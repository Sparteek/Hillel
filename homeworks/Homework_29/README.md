# Homework 29 — PostgreSQL and Docker

Усі ресурси мають префікс `hw29_`, тому їх легко відрізнити від інших контейнерів.

## 1. Створити окрему мережу

```powershell
docker network create --label homework=29 hw29_network
```

## 2. Запустити PostgreSQL

```powershell
docker run -d --name hw29_postgres --label homework=29 --network hw29_network -e POSTGRES_DB=homework29 -e POSTGRES_USER=hw29_user -e POSTGRES_PASSWORD=hw29_password -v hw29_postgres_data:/var/lib/postgresql/data postgres:15-alpine
```

## 3. Збудувати образ застосунку

```powershell
docker build -t hw29_db_app .
```

## 4. Запустити тести в контейнері

```powershell
docker run --name hw29_tests --label homework=29 --network hw29_network -e POSTGRES_HOST=hw29_postgres -e POSTGRES_PORT=5432 -e POSTGRES_DB=homework29 -e POSTGRES_USER=hw29_user -e POSTGRES_PASSWORD=hw29_password hw29_db_app
```

Тести перевіряють підключення, INSERT, SELECT, UPDATE і DELETE.
