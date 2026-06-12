

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'
    @staticmethod
    def sount():
        print('Mewooooo')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'I\'m dog: {self.name}, {self.age}'

    @staticmethod
    def sound():
        print('Gaaaav')

class CatDog(Dog, Cat):
    def __init__(self, name, age):
        #super().__init__(name, age)
        Cat.__init__(self, name, age)
        Dog.__init__(self, name, age)

cat_dog = CatDog('Cat_Dog', 18)
print(cat_dog.__str__()) #Найближчий класс собака, тому видасть собаку
print(cat_dog.sound())

print(CatDog.mro())
print(CatDog.__mro__) #Тут ми зможемо це подивитися... 