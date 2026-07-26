
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS products (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    category_id INTEGER NOT NULL REFERENCES categories(id)
);


TRUNCATE TABLE products, categories RESTART IDENTITY CASCADE;


INSERT INTO categories (name)
VALUES
    ('Ноутбуки'),
    ('Смартфони'),
    ('Навушники');


INSERT INTO products (name, description, price, category_id)
VALUES
    ('Lenovo IdeaPad', 'Ноутбук для роботи', 25000.00, 1),
    ('Samsung Galaxy', 'Смартфон Android', 18000.00, 2),
    ('Sony WH-1000XM5', 'Бездротові навушники', 14000.00, 3);


SELECT
    p.id,
    p.name AS product_name,
    p.description,
    p.price,
    c.name AS category_name
FROM products AS p
JOIN categories AS c
    ON p.category_id = c.id
ORDER BY p.id;
