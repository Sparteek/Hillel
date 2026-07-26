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
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                name TEXT NOT NULL,
                course TEXT NOT NULL
            )
            """
        )

        cursor.execute(
            "INSERT INTO students (name, course) VALUES (%s, %s) RETURNING id",
            ("Student", "Python Pro"),
        )
        student_id = cursor.fetchone()[0]

        cursor.execute(
            "SELECT id, name, course FROM students WHERE id = %s",
            (student_id,),
        )
        print(cursor.fetchone())
