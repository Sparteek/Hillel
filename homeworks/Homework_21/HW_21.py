import random

from faker import Faker
from sqlalchemy import select

from db import Base, Session, engine
from orm_courses_table import OrmCourse
from orm_students_table import OrmStudent


fake = Faker("uk_UA")

COURSE_NAMES = [
    "IT General",
    "Python",
    "Java AT",
    "SQL",
    "QA Manual",
]


def create_tables():
    """Створює таблиці courses і students, якщо їх ще немає."""
    Base.metadata.create_all(engine)
    return "Таблиці courses і students готові."


def create_courses():
    """Додає п'ять курсів."""
    with Session() as session:
        existing_course_names = set(
            session.scalars(select(OrmCourse.name)).all()
        )

        courses = [
            OrmCourse(name=course_name)
            for course_name in COURSE_NAMES
            if course_name not in existing_course_names
        ]
        session.add_all(courses)
        session.commit()
        return f"Додано нових курсів: {len(courses)}."


def create_random_students(students_count=20):
    """    Створює 20 людей. Якщо людина навчається на декількох курсах, для неї створюється
    окремий рядок у students для кожного курсу. """
    with Session() as session:
        first_student = session.scalars(
            select(OrmStudent)
        ).first()

        if first_student is not None:
            return "Студентів не створено: таблиця students уже має записи."

        courses = session.scalars(select(OrmCourse)).all()

        students = []

        for _ in range(students_count):
            student_name = fake.name()
            student_age = random.randint(18, 45)
            selected_courses = random.sample(
                courses,
                k=random.randint(1, 3),
            )

            for course in selected_courses:
                students.append(
                    OrmStudent(
                        name=student_name,
                        age=student_age,
                        course=course,
                    )
                )

        session.add_all(students)
        session.commit()
        return (
            f"Створено людей: {students_count}. "
            f"Додано записів у students: {len(students)}."
        )


def add_student_to_course(student_name, student_age, course_name):
    """Додає один запис студента на один курс."""
    with Session() as session:
        course = session.scalars(
            select(OrmCourse).where(
                OrmCourse.name == course_name
            )
        ).first()

        if course is None:
            return f"Помилка: курс {course_name!r} не знайдений."

        existing_student = session.scalars(
            select(OrmStudent).where(
                OrmStudent.name == student_name,
                OrmStudent.course_id == course.id,
            )
        ).first()

        if existing_student is not None:
            return (
                f"{student_name!r} уже зареєстрований "
                f"на курс {course_name!r}."
            )

        student = OrmStudent(
            name=student_name,
            age=student_age,
            course=course,
        )

        session.add(student)
        session.commit()
        return (
            f"Студента {student_name!r} додано "
            f"на курс {course_name!r}."
        )


def get_students_by_course(course_name):
    """Повертає студентів, зареєстрованих на певний курс."""
    with Session() as session:
        query = (
            select(OrmStudent)
            .join(OrmCourse)
            .where(OrmCourse.name == course_name)
        )
        return session.scalars(query).all()


def get_courses_by_student(student_name):
    """Повертає курси, на яких навчається певний студент."""
    with Session() as session:
        query = (
            select(OrmCourse)
            .join(OrmStudent)
            .where(OrmStudent.name == student_name)
        )
        return session.scalars(query).all()


def update_student_age(student_name, new_age):
    """Оновлює вік у всіх рядках певного студента."""
    with Session() as session:
        students = session.scalars(
            select(OrmStudent).where(
                OrmStudent.name == student_name
            )
        ).all()

        for student in students:
            student.age = new_age

        session.commit()
        if not students:
            return f"Студента {student_name!r} не знайдено."

        return (
            f"Вік студента {student_name!r} оновлено до {new_age}. "
        )


def update_course_name(old_name, new_name):
    """Оновлює назву курсу."""
    with Session() as session:
        course_with_new_name = session.scalars(
            select(OrmCourse).where(
                OrmCourse.name == new_name
            )
        ).first()

        if course_with_new_name is not None:
            return f"Курс {new_name!r} уже існує."

        course = session.scalars(
            select(OrmCourse).where(
                OrmCourse.name == old_name
            )
        ).first()

        if course is None:
            return f"Курс {old_name!r} не знайдений."

        course.name = new_name
        session.commit()
        return f"Курс {old_name!r} перейменовано на {new_name!r}."


def delete_student(student_name):
    """Видаляє всі рядки певного студента."""
    with Session() as session:
        students = session.scalars(
            select(OrmStudent).where(
                OrmStudent.name == student_name
            )
        ).all()

        for student in students:
            session.delete(student)

        session.commit()
        if not students:
            return f"Студента {student_name!r} не знайдено."

        return (
            f"Студента {student_name!r} видалено. "
            f"Видалено рядків: {len(students)}."
        )
