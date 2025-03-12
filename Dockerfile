# Используем официальный образ Python из Docker Hub
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости, необходимые для работы скрипта
RUN pip install --no-cache-dir requests python-telegram-bot schedule

# Копируем текущую директорию в рабочую директорию контейнера
COPY . .

# Команда для запуска скрипта
# CMD ["python", "main.py"]