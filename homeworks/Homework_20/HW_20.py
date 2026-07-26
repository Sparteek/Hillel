import os

import psycopg


connection_settings = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": int(os.getenv("POSTGRES_PORT", "5432")),
    "dbname": os.getenv("POSTGRES_DB", "education_platform"),
    "user": os.getenv("POSTGRES_USER", "teacher"),
    "password": os.getenv("POSTGRES_PASSWORD", "super_password"),
}


with psycopg.connect(**connection_settings) as connection:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                price NUMERIC(10, 2) NOT NULL,
                category_id INTEGER NOT NULL REFERENCES categories(id)
            )
            """
        )

        cursor.execute(
            "TRUNCATE TABLE products, categories RESTART IDENTITY CASCADE"
        )

        cursor.executemany(
            "INSERT INTO categories (name) VALUES (%s)",
            [
                ("Ноутбуки",),
                ("Смартфони",),
                ("Навушники",),
            ],
        )

        cursor.executemany(
            """
            INSERT INTO products (name, description, price, category_id)
            VALUES (%s, %s, %s, %s)
            """,
            [
                ("Lenovo IdeaPad", "Ноутбук для роботи", 25000.00, 1),
                ("Samsung Galaxy", "Смартфон Android", 18000.00, 2),
                ("Sony WH-1000XM5", "Бездротові навушники", 14000.00, 3),
            ],
        )

