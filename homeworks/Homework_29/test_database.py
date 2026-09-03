from database import (
    delete_result,
    get_connection,
    insert_result,
    select_result,
    update_result,
)


def test_database_connection():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            assert cursor.fetchone()[0] == 1


def test_insert_and_select_result(saved_result):
    result = select_result(saved_result)

    assert result == (saved_result, "docker database test", "created")


def test_update_result(saved_result):
    assert update_result(saved_result, "passed") is True
    assert select_result(saved_result)[2] == "passed"


def test_delete_result():
    result_id = insert_result("record for deletion", "created")

    assert delete_result(result_id) is True
    assert select_result(result_id) is None
