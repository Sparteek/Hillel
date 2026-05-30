#Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

word = input('Some word: ')
while ('h' not in word and 'H' not in word):
        word =input('without "h" or "H", Try again: ')
print('Success')

