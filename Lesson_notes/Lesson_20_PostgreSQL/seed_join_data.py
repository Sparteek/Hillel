import os
from decimal import Decimal

import psycopg
from faker import Faker


fake = Faker("en_US")

connection_settings = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": int(os.getenv("POSTGRES_PORT", "5432")),
    "dbname": os.getenv("POSTGRES_DB", "education_platform"),
    "user": os.getenv("POSTGRES_USER", "teacher"),
    "password": os.getenv("POSTGRES_PASSWORD", "super_password"),
}

category_names = [
    "Electronics",
    "Books",
    "Home",
    "Sports",
    "Toys",
    "Seasonal",
]


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
                description TEXT NOT NULL,
                price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
                stock INTEGER NOT NULL CHECK (stock >= 0),
                category_id INTEGER REFERENCES categories(id) ON DELETE SET NULL
            )
            """
        )

        # Очищаємо лише навчальні таблиці, щоб повторний запуск створив нові дані.
        cursor.execute("TRUNCATE products, categories RESTART IDENTITY CASCADE")

        category_ids = []
        for category_name in category_names:
            cursor.execute(
                "INSERT INTO categories (name) VALUES (%s) RETURNING id",
                (category_name,),
            )
            category_ids.append(cursor.fetchone()[0])

        # Seasonal навмисно лишається без продуктів для прикладу LEFT JOIN.
        assignable_category_ids = category_ids[:-1]
        products = []

        for index in range(24):
            product_name = (
                f"{fake.word().title()} "
                f"{fake.random_element(elements=('Pro', 'Mini', 'Max', 'Plus', 'Eco'))}"
            )
            price = Decimal(fake.random_int(min=500, max=99900)) / 100
            category_id = (
                None
                if index % 8 == 0
                else fake.random_element(elements=assignable_category_ids)
            )
            products.append(
                (
                    product_name,
                    fake.sentence(nb_words=8),
                    price,
                    fake.random_int(min=0, max=100),
                    category_id,
                )
            )

        cursor.executemany(
            """
            INSERT INTO products (name, description, price, stock, category_id)
            VALUES (%s, %s, %s, %s, %s)
            """,
            products,
        )

        cursor.execute("SELECT COUNT(*) FROM categories")
        categories_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM products")
        products_count = cursor.fetchone()[0]

print(f"Created {categories_count} categories and {products_count} products")
