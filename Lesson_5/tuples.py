# my_tuple = (1, 2, 3, 4, 5,6,7,8,9,10)
#
#
# print(my_tuple)
# my_tuple2 =(my_tuple, 1)
# print(my_tuple2)
#
# def my_function():
#     return 1, 2
#
# print(my_function())
#
# print(my_tuple[:8])
# print(my_tuple2[-1])

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first_element, other_element, *last_element = my_tuple
print(first_element)
print(other_element)
print(last_element)

# first_variable = my_tuple[0]
# last_variable = my_tuple[-1]



var_1 = 5
var_2 = 6
var_1, var_2 = var_2, var_1
print(var_1)
print(var_2)


my_string = "Привіт, світ!"
list = [1, 2, 3]
tuple_from_string = tuple([my_string])
format_to_tuple = tuple(list)
print(format_to_tuple)
