FROM python:3.11-slim

# Установка Poetry
RUN pip install --upgrade pip \
 && pip install poetry

# Установка зависимостей
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false \
 && poetry install --no-root --only main

# Копируем приложение
COPY ./fastapi-application /app/app

# Команда запуска
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
