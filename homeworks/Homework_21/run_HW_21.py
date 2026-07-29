from HW_21 import (
    add_student_to_course,
    create_courses,
    create_random_students,
    create_tables,
    delete_student,
    get_courses_by_student,
    get_students_by_course,
    update_course_name,
    update_student_age,
)


print(create_tables())
print(create_courses())
print(create_random_students())

print(add_student_to_course("Ваня", 25, "Python"))
print(add_student_to_course("Коля", 25, "SQL"))

python_students = get_students_by_course("Python")
print(f"Студенти курсу Python: {len(python_students)}")
for student in python_students:
    print(student)

kolya_courses = get_courses_by_student("Коля")
print(f"Курси Колі: {len(kolya_courses)}")
for course in kolya_courses:
    print(course)

print()
print(update_student_age("Коля", 26))

print()
print(add_student_to_course("Тестовий студент",30,"QA Manual",))
print(delete_student("Тестовий студент"))

# Приклад перейменування курсу:
# print(update_course_name("Java AT", "JavaScript AT"))
