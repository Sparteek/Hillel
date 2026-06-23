#Відокремив тести і доп функції в окремий файл
from homeworks.Homework_13.login_system import log_event



def get_message(user,  status):
        return f"Login event - Username: {user}, Status: {status}"

def read_logs(file_log):
    with open(file_log, "r") as file_log:
        return file_log.read()

def clear_log_file(): #функція очищення логів
    open("login_system.log", "w").close()

def check_log_event(user, status):
    log_event(user, status)
    logs = read_logs("login_system.log")
    message = get_message(user, status)

    assert message in logs

def setup_module(): #це модуль який очищення  логу перед кожним запуском тестів
    clear_log_file()

#поділив на окремі тести, для зручності.
def test_log_event_success():
    check_log_event("user1", "success")


def test_log_event_expired():
    check_log_event("user2", "expired")

def test_log_event_failed():
    check_log_event("user3", "failed")