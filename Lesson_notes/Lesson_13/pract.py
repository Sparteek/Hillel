# Напишіть функцію capitalize_text, яка приймає рядок тексту і повертає цей же текст, але з першою великою і іншими маленькими літерами для кожного слова.

input_value = ('good, Bad, UGLY')

def capitalize_text(text):
    return text.title()

print(capitalize_text(input_value))


def word_count(text):
    return len(text.split())

print(word_count('I want to be free, but not always'))

def concatenate_strings(strings, separator):
    if strings == [""]:
       return "List is empty"
    else:
        return separator.join(strings)
    return result

strings = ["Bla, Bla, Bala", "Be Be Be"]
print(concatenate_strings(strings, ", "))
print(concatenate_strings(strings, " - "))

