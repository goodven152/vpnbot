#!/bin/bash

# Остановить и удалить существующие контейнеры
docker-compose down

# Удалить контейнеры и сети, связанные с проектом
docker-compose rm -f

# # Удалить все скачанные образы
docker image prune -a -f

# docker volume create

# Собрать и запустить контейнеры
docker-compose up -d

# Проверить статус контейнеров
docker-compose ps
