
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer_task1 = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer_task1)


# task 02 ==
""" Замініть .... на пробіл """
adwentures_of_tom_sawer_task2 = adwentures_of_tom_sawer_task1.replace("....", " ")
print(adwentures_of_tom_sawer_task2)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами."""
adwentures_of_tom_sawer_task3 = " ".join(adwentures_of_tom_sawer_task2.split())
print(adwentures_of_tom_sawer_task3)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h" """
count_h = 0
for h in adwentures_of_tom_sawer_task3:
    if h == "h":
        count_h += 1
print(f'{count_h} разів у тексті зустрічається літера "h"')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?"""
adwentures_of_tom_sawer_task4 = adwentures_of_tom_sawer_task3.split()
count_upper = 0
for words in adwentures_of_tom_sawer_task4:
    if words[0].isupper():
        count_upper += 1
print(f'{count_upper} слів у тексті починається з Великої літери')


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге"""
index_1 = adwentures_of_tom_sawer_task3.find("Tom")
index_2 = adwentures_of_tom_sawer_task3.find("Tom", index_1 + 1)
print(f'Слово "Tom" вдруге зустрічається на {index_2} позиції')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer_task3.rstrip(".").split(".") #тут rstrip прибрати '' в кінці строки
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentences_4 = adwentures_of_tom_sawer_sentences[3].lower()
print(sentences_4)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for task_9 in adwentures_of_tom_sawer_sentences:
    task_9 = task_9.strip() #Прибрати пробіл який виник перед "By"
    if task_9.startswith("By the time"):
        print(task_9)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence_words = adwentures_of_tom_sawer_sentences[-1].split()
print(f'{len(last_sentence_words)} слів в останньому реченні')
