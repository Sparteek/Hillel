import os
import time

import psycopg2
from psycopg2 import OperationalError


DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": os.getenv("POSTGRES_PORT", "5432"),
    "dbname": os.getenv("POSTGRES_DB", "homework29"),
    "user": os.getenv("POSTGRES_USER", "hw29_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "hw29_password"),
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def wait_for_database(attempts=30, delay=1):
    for attempt in range(1, attempts + 1):
        try:
            connection = get_connection()
            connection.close()
            return
        except OperationalError:
            if attempt == attempts:
                raise
            time.sleep(delay)


def create_table():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS test_results (
                    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    test_name TEXT NOT NULL,
                    status TEXT NOT NULL
                )
                """
            )


def insert_result(test_name, status):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO test_results (test_name, status) VALUES (%s, %s) RETURNING id",
                (test_name, status),
            )
            return cursor.fetchone()[0]


def select_result(result_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, test_name, status FROM test_results WHERE id = %s",
                (result_id,),
            )
            return cursor.fetchone()


def update_result(result_id, new_status):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE test_results SET status = %s WHERE id = %s RETURNING id",
                (new_status, result_id),
            )
            return cursor.fetchone() is not None


def delete_result(result_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM test_results WHERE id = %s RETURNING id",
                (result_id,),
            )
            return cursor.fetchone() is not None
