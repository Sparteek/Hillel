# new_value = input('Enter some text:')
#
# print(new_value)
# print(type(new_value))
# print( int(new_value) ** 2)

# str_value = '12 3123 123 a'
#
# print(id(str_value))
#
# int_value = str_value + '123 123123 213123'
# print(id(int_value))
#
# int_value = 1
# print(id(int_value))
#
# int_value += 5
# print(id(int_value))

list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(id(list_of_elements))
list_of_elements.append(6)
print(id(list_of_elements))

def my_function(value:int = 1, list_elements: list = None):
    if list_elements is None:
        list_ = []
    list_aftter_adding.append(value)
    return list_after_adding
print(my_function())
print(my_function(value = 5))