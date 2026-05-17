# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
'"That depends a good deal on where you want to get to," said the Cat.\n'
'"I don\'t much care where ——" said Alice.\n'
'"Then it doesn\'t matter which way you go," said the Cat.\n'
'"—— so long as I get somewhere," Alice added as an explanation.\n'
'"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
for literal in alice_in_wonderland:
    if literal == "'":
        print(literal)
print(alice_in_wonderland)


# task 04

"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
azov_sea_area = 37_800
black_sea_area = 436_402
print(f'Чорне та Азовське моря займають {azov_sea_area+black_sea_area} км2 разом')

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

all_items = 375_291
first_and_second_storage = 250_449
second_and_third_storage = 222_950

print(f'На першому складі {all_items - second_and_third_storage} товарів')
print(f'На другому складі {first_and_second_storage - (all_items - second_and_third_storage)} товарів')
print(f'На третьому складі {all_items - first_and_second_storage} товарів')


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

credit_time_months = 18
pay_for_1month_uah = 1179
print(f'Вартість комп’ютера= {credit_time_months * pay_for_1month_uah} грн')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f'Остача від ділення чисел :')
print(f'a:{8019 % 8}   ' 
      f'd:{7248 % 6}   ')
print(f'b:{9907 % 9}   '
      f'e:{7128 % 5}   ')
print(f'c:{2789 % 5}   '
      f'f:{19224 % 9}   ')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
#Припускаю що ціна вказана за одиницю
pizza_xl = 274 * 4
pizza_l = 218 * 2
juice = 4 * 35
cake = 350 * 1
water = 21 * 3

print(f'Іринці знадобиться {pizza_xl+pizza_l+juice+cake+water} грн на її замовлення')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_count = 232
page_photo_limit = 8
pages = photo_count // page_photo_limit
if photo_count % page_photo_limit != 0: #якщо ділення не дасть цілого числа, то необхідна ще одна сторінка
    pages = pages + 1
print(f'Ігорю знадобиться {pages} сторінок щоб, вклеїти всі фото.')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

trip_length_km = 1600
fuel_tank_liters = 48
liter_per_100_km = 9

fuel_needed = trip_length_km / 100 * liter_per_100_km #тут "/" бо якщо буде не ціле число, то неправильно порахує пальне
fuel_stops = fuel_needed // fuel_tank_liters - 1 #виїзд з повним баком, тож не рахуємо як зупинку
if fuel_needed % fuel_tank_liters != 0: # якщо пальне не ділиться рівно на баки, потрібна ще одна заправка
    fuel_stops = fuel_stops + 1
fuel_stops = int(fuel_stops) # Ми отримаємо число без остачі на кількість зупинок.
print(f'Родині знадобиться {fuel_needed} літрів для такої подорожі')
print(f'Родині необхідно заїхати {fuel_stops} рази на заправку')
