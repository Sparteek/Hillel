-- 1. Перевіряємо, до якої бази та під яким користувачем підключилися.
SELECT current_database(), current_user, version();

-- 2. Читаємо всі записи з таблиці.
SELECT id, name, course
FROM students
ORDER BY id;

-- 3. Додаємо запис і одразу отримуємо створений id.
INSERT INTO students (name, course)
SELECT 'Serhii', 'Python Pro'
WHERE NOT EXISTS (
    SELECT 1 FROM students WHERE name = 'Serhii'
)
RETURNING id, name, course;

-- 4. Змінюємо лише щойно доданий запис.
UPDATE students
SET course = 'PostgreSQL Basics'
WHERE name = 'Serhii'
RETURNING id, name, course;

-- 5. Фільтруємо та рахуємо записи.
SELECT course, COUNT(*) AS students_count
FROM students
GROUP BY course
ORDER BY students_count DESC;

-- 6. Видалення. Розкоментуйте, коли захочете потренувати DELETE.
-- DELETE FROM students
-- WHERE name = 'Serhii'
-- RETURNING id, name, course;
