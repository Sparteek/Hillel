#Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть об'єкт цього класу,
# представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.



class Student:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.__average_grade = 76

    def get_average_grade(self):
        return self.__average_grade

    def update_average_grade(self, grade):
        self.__average_grade = grade #я тут використав сама '=' бо в завданні сказано "метод який дозволяє змінювати"

    def show_info(self):
        return f'Name:{self.name}, Last_name:{self.last_name}, Age:{self.age}, Average_grade:{self.get_average_grade()}'

student_1 = Student("John", "Doe", 44)


print(student_1.show_info())
student_1.update_average_grade(55)
print(student_1.show_info())

