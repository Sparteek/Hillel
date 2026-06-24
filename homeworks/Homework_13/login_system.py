"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force = True
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

# def get_message(user,  status):
#         return f"Login event - Username: {user}, Status: {status}"
#
# def read_logs(file_log):
#     with open(file_log, "r") as file_log:
#         return file_log.read()
#
# def clear_log_file():
#     open("login_system.log", "w").close()
#
# def check_log_event(user, status):
#     log_event(user, status)
#     logs = read_logs("login_system.log")
#     message = get_message(user, status)
#
#     assert message in logs
# clear_log_file()
#
# def test_log_event_success():
#     check_log_event("user1", "success")
#
#
# def test_log_event_expired():
#     check_log_event("user2", "expired")
#
# def test_log_event_failed():
#     check_log_event("user3", "failed")
#
