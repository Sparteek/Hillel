import logging

import pytest


logger = logging.getLogger(__name__)

BASE_URL = "http://127.0.0.1:8080"

SEARCH_CASES = [
    ("brand", 3),
    ("brand", 7),
    ("year", 5),
    ("engine_volume", 4),
    ("price", 6),
    ("price", 10),
]


class TestCarSearch:
    @pytest.mark.parametrize(
        "sort_by, limit",
        SEARCH_CASES,
    )
    def test_search_cars(self, auth_session, sort_by, limit):
        logger.info("Пошук машин: sort_by=%s, limit=%s", sort_by, limit)

        response = auth_session.get(
            f"{BASE_URL}/cars",
            params={"sort_by": sort_by, "limit": limit},
            timeout=5,
        )
        assert response.status_code == 200, (
            f"GET /cars повернув статус {response.status_code}"
        )

        cars = response.json()
        assert len(cars) == limit, (
            f"Очікували {limit} машин, отримали {len(cars)}"
        )

        actual_values = [car[sort_by] for car in cars]
        assert actual_values == sorted(actual_values), (
            f"Машини неправильно відсортовані за полем {sort_by}"
        )

        logger.info(
            "Отримано %s машин; %s=%s",
            len(cars),
            sort_by,
            actual_values,
        )
