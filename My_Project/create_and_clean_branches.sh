#!/bin/bash

# Список веток, которые нужно создать и очистить
branches=(
    "FAST-USERS"
    "JWT_AUTH"
    "ficha"
    "Pet_Shop"
    "german"
    "Python"
    "kubik"
    "my"
    "VooDoo"
    "algoritms"
    "app"
    "socket"
    "blog"
    "web-app"
    "class_test"
    "тестирование"
)

# Проходим по каждой ветке
for branch in "${branches[@]}"
do
  # Создаем и переключаемся на ветку
  git checkout -b $branch

  # Удаляем все файлы в ветке
  git rm -r *

  # Коммитим изменения
  git commit -m "Очистка ветки $branch от файлов"

  # Отправляем изменения в удаленный репозиторий
  git push origin $branch
done

