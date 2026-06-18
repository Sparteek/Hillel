# try:
#     # Код, який може викликати помилку
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Помилка: ділення на нуль")
# finally:
#     print("Цей блок завжди виконується, незалежно від того, чи виникла помилка чи ні")
#
# def divide_numbers(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("Помилка: Ділення на нуль.")
#     else:
#         print(f"Результат ділення {a} на {b}: {result}")
#
# # Приклад виклику функції
# divide_numbers(10, 2)
# divide_numbers(5, 0)


# def divide_numbers(a, b):
#     try:
#         result = a / b
#         print(result)
#
#         [1, 2, 3, 4, 5][455]
#
#     except ZeroDivisionError as e:
#         print('ZeroDivisionError')
#         print(e)
#
#     except IndexError as i:
#         print('IndexError')
#         print(i)
#
#
# divide_numbers(10, 2)
#
#
def db_connect():
    print('db_connect')

def db_disconnect():
    print('db_disconnect')

def sql_query():
    print('sql_query')
    raise TypeError

def db_work():
    try:
        db_connect()
        sql_query()
        db_disconnect()

    except TypeError as e:
        print('TypeError')
        db_disconnect()

    except Exception as e:
        print('TypeError')
        db_disconnect()


