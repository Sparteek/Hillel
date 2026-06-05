# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            break
            # Enter the action to take if the result is greater than 25

        else:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
        # Increment the appropriate variable


multiplication_table(3)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_function(value1, value2):
    sum_value = value1 + value2
    return sum_value
print(sum_function(1, 9))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
numbers = [10,1,4,5,6,7]

def average_function(numbers):
    if numbers == []:
        return f'The list is empty {numbers}'

    average = sum(numbers) / len(numbers)
    return average
print(average_function(numbers))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

value ="Hello, world!"
def reversed_function(value):
    reversed_value = value[::-1]
    return reversed_value
print(reversed_function(value))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
words = ['Hello', 'World', 'Tartartfsffsafafs', 'Gradddppedd']
#Якщо у списці будуть два найдовші слова то виведе перше знайдене, і не замінить черз "len(word) >"
def longest_word(words):
    longest_word = words[0]
    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
print(longest_word(words))



# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    result = str1.find(str2)
    return result

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
#Порахувати суму усіх парних чисел

# even_number_sum = 0
#
# for number in numbers:
#     if number % 2 == 0:
#         even_number_sum += number
# print(f'Sum of even numbers: {even_number_sum}')

def sum_even_numbers(numbers):
    """Returns the sum of even numbers from a list."""
    even_number_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_number_sum += number
    return even_number_sum

print(sum_even_numbers([30,40,3,5]))
print(sum_even_numbers([4,5,6]))

# task 8
#Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими


# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# lst2 = []
#
# for item in lst1:
#     if  isinstance(item, str):
#         lst2.append(item)
# print(lst2)
def create_string_list(lst):
    """Returns a new list containing only string elements from the given list."""
    lst2 = []
    for item in lst:
        if isinstance(item, str):
            lst2.append(item)
    return lst2
print(create_string_list(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']))
# task 9
# data = input("input the data:")
# UNIQUE_ELEMENTS_LIMIT = 10
#
# if len(set(data)) > UNIQUE_ELEMENTS_LIMIT:
#     print(True)
# else:
#     print(False)

def unique_elements_limit(data):
    """Checks if the number of unique elements in data is greater than 10."""
    UNIQUE_ELEMENTS_LIMIT = 10

    if len(set(data)) > UNIQUE_ELEMENTS_LIMIT:
        return True
    else:
        return False
print(unique_elements_limit([10,9,9,4,5,6,7,17,13,1,1,3,4,5,6,7,8]))
print(unique_elements_limit([1,2,3,4,4,4,4]))

# task 10
# """ Перевірте чи починається якесь речення з "By the time".
# """
# for task_9 in adwentures_of_tom_sawer_sentences:
#     task_9 = task_9.strip() #Прибрати пробіл який виник перед "By"
#     if task_9.startswith("By the time"):
#         print(task_9)

def check_start_sentence(text):
    """Returns sentences from the text that start with 'So'."""
    result = []
    sentences = text.split('.')

    for sentence in sentences:
        sentence = sentence.strip()

        if sentence.startswith ("So"):
            result.append(sentence)
    return result
print(check_start_sentence("So we goint to park. Then goint to show. So I`ill be busy"))


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""