import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"


@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()

    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass"),
        timeout=5,
    )
    assert response.status_code == 200, (
        f"Помилка авторизації: {response.status_code}, {response.text}"
    )
    token = response.json()["access_token"]

    session.headers.update({"Authorization": f"Bearer {token}"})

    yield session

    session.close()

