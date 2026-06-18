
user_result = {'id': 1, 'name':' ', 'age':24, 'avr_score': None, 'subject':5, 'score': 334 }


def my_func(user_resul: dict):
    age, score, subject, avr_subject = user_resul['age'], user_resul['score'], user_resul['subject'], user_resul['avr_score']
    if not(18 < age < 65):
        raise ValueError('User has to be from 18 to 65')

    if score / subject == avr_subject:
        raise ValueError('Not equal data')


my_func(user_result)