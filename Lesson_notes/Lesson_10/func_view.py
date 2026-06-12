name = 'Vlad'


def greeting():
    name = 'Vika'
    print(f'Hello, {name}!')

def greeting_1():
    def return_name_with():
        return name + '_smth'
    print(return_name_with())


class Greeting:
    name = 'Alex'

class Greeting2:
    name = 'Vika'

greeting_1()

# greeting_1 = Greeting()
# greeting_2 = Greeting2()
#
# print(greeting_1.name)
# print(greeting_2.name)