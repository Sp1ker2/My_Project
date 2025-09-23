# 🐍 Python Monorepo: Backend Playground

Этот монорепозиторий содержит множество Python-проектов и модулей, предназначенных для экспериментов, разработки и тестирования различных подходов в backend-разработке.

## 📁 Структура

### `FAST-USERS/`
Проект на **FastAPI** с авторизацией, WebSocket и миграциями через Alembic.
- `auth/` — авторизация и управление пользователями.
- `cours/` — функциональность по курсам.
- `socket/` — WebSocket сервер и клиент (index.html, js).
- `migrations/` — Alembic миграции.
- `main.py` — запуск приложения.

### `JWT_AUTH/`
FastAPI-проект с JWT-аутентификацией и системой заказов/профилей.
- `api_v1/` — API-модули: авторизация, продукты.
- `core/models/` — ORM модели: пользователь, продукт, заказ.
- `alembic/` — миграции.
- Используется Poetry (`pyproject.toml`).

### `Pet_Shop/`
**Django**-проект для зоомагазина.
- `pets/` — модели, сериализаторы, представления.
- Поддержка Docker: `Dockerfile`, `docker-compose.yml`.
- Postman коллекция: `Pets_Shop.postman_collection.json`.

### `fastapi-application/`
Минималистичный FastAPI-прототип с модулями, схемами и Alembic.
- `api/api_v1/users.py` — пользовательский API.
- `core/models/` — ORM + миксины.
- `utils/` — утилиты, генераторы шаблонов и форматирование.

### `web-app/`
Django веб-приложение с интерфейсами новостей, шаблонами и статикой.

### `app/`
Модульное FastAPI-приложение с категориями, постами и тегами.

### `blog/`
Фронтенд-блог на Flask или FastAPI (разметка на Jinja, CSS, HTML).

### `algoritms/`
Набор лабораторных по алгоритмам:
- `lab01` → Linked List.
- `lab02–lab07` → базовые структуры и сортировки.

### `ficha/`
Классические алгоритмы:
- Быстрая сортировка, бинарный поиск, Евклид и др.

### `class_test/`, `тестирование/`
Модули и тесты для обучения ООП, unit-тестирования.

### `german/`
HTML-проект (сайт-магазин на чистом HTML/CSS/JS), включая SQL и PHP.

### `VooDoo/`, `my/`, `kubik/`
Разрозненные модули и скрипты для разных целей (парсеры, алгоритмы, ML и пр.)

# 📌 CRM Application

Лёгкая CRM-система на **FastAPI** с авторизацией, клиентами и пользователями.  
Использует **PostgreSQL** в качестве базы данных, **Alembic** для миграций и запускается через **Docker Compose**.

---

## ⚙️ Технологии

- ⚡ [FastAPI](https://fastapi.tiangolo.com/) — веб-фреймворк  
- 🐘 [PostgreSQL](https://www.postgresql.org/) — база данных  
- 🛠 [SQLAlchemy](https://www.sqlalchemy.org/) — ORM  
- 🔄 [Alembic](https://alembic.sqlalchemy.org/) — миграции БД  
- 📦 [Poetry](https://python-poetry.org/) — менеджер зависимостей    

---


