import json

import allure

from database import (
    delete_result,
    get_connection,
    insert_result,
    select_result,
    update_result,
)


def attach_result(result):
    """Додає отриманий запис PostgreSQL до Allure-звіту як JSON."""
    result_as_dict = {
        "id": result[0],
        "test_name": result[1],
        "status": result[2],
    }
    allure.attach(
        json.dumps(result_as_dict, ensure_ascii=False, indent=2),
        name="Запис із PostgreSQL",
        attachment_type=allure.attachment_type.JSON,
    )


@allure.epic("Homework 29: Docker and PostgreSQL")
@allure.feature("Database operations")
@allure.story("Database connection")
@allure.title("Підключення до PostgreSQL успішне")
@allure.description("Перевіряє, що контейнер із PostgreSQL приймає SQL-запити.")
@allure.severity(allure.severity_level.CRITICAL)
def test_database_connection():
    with allure.step("Відкрити підключення до PostgreSQL"):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()[0]

    with allure.step("Виконати контрольний SQL-запит SELECT 1"):
        assert result == 1

    with allure.step("Додати результат запиту до звіту"):
        allure.attach(
            "SELECT 1 returned 1",
            name="Перевірка підключення",
            attachment_type=allure.attachment_type.TEXT,
        )


@allure.epic("Homework 29: Docker and PostgreSQL")
@allure.feature("Database operations")
@allure.story("Create and read a test result")
@allure.title("Збереження та читання результату тесту")
@allure.description("Перевіряє, що створений запис можна отримати за його id.")
@allure.severity(allure.severity_level.NORMAL)
def test_insert_and_select_result(saved_result):
    with allure.step("Отримати створений запис за його id"):
        result = select_result(saved_result)

    with allure.step("Додати отриманий запис до Allure-звіту"):
        attach_result(result)

    with allure.step("Перевірити дані збереженого запису"):
        assert result == (saved_result, "docker database test", "created")


@allure.epic("Homework 29: Docker and PostgreSQL")
@allure.feature("Database operations")
@allure.story("Update a test result")
@allure.title("Оновлення статусу результату тесту")
@allure.description("Перевіряє зміну статусу запису з created на passed.")
@allure.severity(allure.severity_level.NORMAL)
def test_update_result(saved_result):
    with allure.step("Оновити статус запису на passed"):
        is_updated = update_result(saved_result, "passed")

    with allure.step("Отримати оновлений запис"):
        result = select_result(saved_result)

    with allure.step("Додати оновлений запис до Allure-звіту"):
        attach_result(result)

    with allure.step("Перевірити новий статус"):
        assert is_updated is True
        assert result[2] == "passed"


@allure.epic("Homework 29: Docker and PostgreSQL")
@allure.feature("Database operations")
@allure.story("Delete a test result")
@allure.title("Видалення результату тесту")
@allure.description("Перевіряє, що видалений запис більше не повертається з бази.")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_result():
    with allure.step("Створити запис для видалення"):
        result_id = insert_result("record for deletion", "created")

    with allure.step("Видалити створений запис"):
        is_deleted = delete_result(result_id)

    with allure.step("Переконатися, що запис відсутній у базі"):
        result = select_result(result_id)

    with allure.step("Додати результат видалення до Allure-звіту"):
        allure.attach(
            json.dumps({"deleted_id": result_id, "record_after_deletion": result}),
            name="Результат видалення",
            attachment_type=allure.attachment_type.JSON,
        )

    with allure.step("Підтвердити успішне видалення"):
        assert is_deleted is True
        assert result is None
