# # def sep_function():
# #     print('*' * 80)
# #     print('Hello word')
# #     print('*' * 80)
# #
# #
#  def sep_function_2(value_1: int | float, value_2: int | float): #який тип данних може прийти в цю змінну
# #     print('*' * 80)
# #     print(f'{value_1} * {value_2} = {value_1 * value_2}')
# #     print('-' * 80)
# #
# # sep_function_2(value_1=1, value_2=2)
# # sep_function_2(1, 2)
# # sep_function_2(value_1=5, value_2=2)
# #
# # print(sep_function_2(value_1=5, value_2=2))
#
# def sum_value_with_return(value1, value2):
#    sum_value = value1 + value2
#
#    return sum_value, value1, value2
#
# print(sum_value_with_return(1, 2))

def hell(name, surname, nickname = None):
    if nickname:
        print(f'{name} {surname} {nickname}')
    else:
        print(f'Hello {name} {surname}!')

hello(name='John')