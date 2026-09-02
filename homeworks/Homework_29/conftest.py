import pytest

from database import create_table, delete_result, insert_result, wait_for_database


@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    wait_for_database()
    create_table()


@pytest.fixture
def saved_result():
    result_id = insert_result("docker database test", "created")
    yield result_id
    delete_result(result_id)
