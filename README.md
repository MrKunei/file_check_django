 <b>_File cheсking_</b> — осуществляет проверку файлов через flake8 и отправляет отчет на email.

---

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Celery](https://img.shields.io/badge/-Celery-464646?style=flat-square&logo=Celery)](https://www.celeryq.dev/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

---


## Функционал:
* Регистрация/Авторизация;
* Загрузка файлов;
* Автоматическая проверка файлов со статусом новый или измененный на соответствие flake8;
* Автоматическая отправка отчетов о результате проверки на email и изменение статуса;
---

## Локальный запуск:

  Склонируйте репозиторий.

  Находясь в папке с кодом создайте виртуальное окружение `python -m venv venv`;
  
  Активируйте виртуальное окружение (Windows: `source venv\scripts\activate`; Linux/Mac: `source venv/bin/activate`);

  Установите зависимости `python -m pip install -r requirements.txt`.

  Переименуйте `.env.example` в `.env` и заполните его.

  Для локального запуска, находясь в директории проекта выполните команды:
  ```
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
  ```

## Запуск проекта через Docker

Перейдите в корневую папку проекта где находится файл `docker-compose.yaml` и выполните команду:

```
docker-compose up -d --build
```
