#замість теста додатково напишть
# Завдання 1
# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
# які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут
# programming_language.
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути як
# Manager (ім('я, зарплата, відділ), '
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.)
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

    def __str__(self):
        return (f'TeamLead:{self.name}, team_size: {self.team_size}, department: {self.department}, '
                f'programming language: {self.programming_language}, salary: {self.salary} ')

team_lead_1 = TeamLead(team_size=12, name='Leha', department= 'IT', programming_language='Python', salary=20000)
print(team_lead_1)
print(TeamLead.mro())

#тест атрібутів
assert hasattr(team_lead_1, "name")
assert hasattr(team_lead_1, "salary")
assert hasattr(team_lead_1, "department")
assert hasattr(team_lead_1, "programming_language")
assert hasattr(team_lead_1, "team_size")
print("All tests passed")

# Завдання 2
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod
