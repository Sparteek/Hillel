-- Зв'язок: одна категорія може мати багато продуктів.
-- products.category_id посилається на categories.id.

-- 1. INNER JOIN: тільки продукти, які мають категорію.
SELECT
    p.id,
    p.name AS product_name,
    p.price,
    p.stock,
    c.name AS category_name
FROM products AS p
JOIN categories AS c ON c.id = p.category_id
ORDER BY c.name, p.name;

-- 2. INNER JOIN із фільтром: дорогі продукти разом із категоріями.
SELECT
    p.name AS product_name,
    p.price,
    c.name AS category_name
FROM products AS p
JOIN categories AS c ON c.id = p.category_id
WHERE p.price >= 500
ORDER BY p.price DESC;

-- 3. LEFT JOIN від products: показує також продукти без категорії.
SELECT
    p.name AS product_name,
    p.price,
    COALESCE(c.name, 'Без категорії') AS category_name
FROM products AS p
LEFT JOIN categories AS c ON c.id = p.category_id
ORDER BY p.id;

-- 4. LEFT JOIN від categories: показує навіть порожні категорії.
SELECT
    c.name AS category_name,
    COUNT(p.id) AS products_count,
    ROUND(AVG(p.price), 2) AS average_price
FROM categories AS c
LEFT JOIN products AS p ON p.category_id = c.id
GROUP BY c.id, c.name
ORDER BY products_count DESC, c.name;

-- 5. Категорії, в яких немає жодного продукту.
SELECT c.id, c.name
FROM categories AS c
LEFT JOIN products AS p ON p.category_id = c.id
WHERE p.id IS NULL;

-- 6. Продукти, яким не призначили категорію.
SELECT p.id, p.name, p.price
FROM products AS p
LEFT JOIN categories AS c ON c.id = p.category_id
WHERE c.id IS NULL;

-- Завдання для самостійної практики:
-- A. Вивести продукти категорії Electronics, від дорожчих до дешевших.
-- B. Порахувати сумарний stock продуктів у кожній категорії.
-- C. Показати лише категорії, де є щонайменше три продукти.
