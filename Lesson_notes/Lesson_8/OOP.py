class Cat:

    def sound(self):
        print('Meow')


    def run(self):
        print('Im running')




cat_2 = Cat()
cat_2.sound()



class Children:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def inizialization(cls, name, age):
        import datetime
        datetime = datetime.datetime.now().year
        age = datetime - age
        return cls(name, age)

alex = Children('Alex', 10)

vasya = Children.inizialization(name='Vasya', age=2010)

print(vasya.age)