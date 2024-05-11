# Первый этап: Создание базового образа с OpenCV
FROM python:3.12-slim as base-opencv

# Установка необходимых пакетов для OpenCV
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-opencv libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка pip
RUN pip install --upgrade pip

# Этот образ будет использоваться в будущих сборках