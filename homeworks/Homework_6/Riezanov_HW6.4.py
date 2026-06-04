#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті


#numbers = [12, 7, 3, 18, 25, 40, 9, 2, 11, 6, 15, 30, 10, 5]\
numbers = [10,5,14,44,55,66,7]
even_number_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_number_sum += number
print(f'Sum of even numbers: {even_number_sum}')
