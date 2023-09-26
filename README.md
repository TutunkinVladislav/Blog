# Блог о кино

![example workflow](https://github.com/TutunkinVladislav/Blog/actions/workflows/blog_tests.yml/badge.svg)

Данный проект предназначен для просмотра информации о различных фильмах. На сайте можно прочитать описание фильма, узнать жанр, страну, год выхода, продожительность. Также можно посмотреть актёров, которые снимались в определлёном фильме и узнать режиссёра, который снял этот фильм.

Также авторизовавшись можно оставлять комментарии к фильмам.

### Стек:
- Python 3.9
- Django 3.2.10
- Pillow 10.0
- SQLite

При push в ветку main автоматически отрабатывает сценарий:
* *tests* - проверка кода на соответствие стандарту PEP8 и запуск unittest.

### Запуск проекта

### Установка и запуск проекта

1. Склонируйте репозиторий;
2. Находясь в папке с кодом создайте виртуальное окружение `python -m venv venv`;
3. Активируйте виртуальное окружение (Windows: `source venv\scripts\activate`; Linux/Mac: `sorce venv/bin/activate`);
4. Установите зависимости `python -m pip install -r requirements.txt`.

Для запуска сервера разработки, находясь в директории проекта, выполните команды:
```
python manage.py migrate
python manage.py runserver
```

Проект будет доступен по адресу:
`http://127.0.0.1:8000/films/`

### Запустить проект с помощью Docker

После клонирования репозитория, переходим в дерикторию где находится Dockerfile, и через терминал запускаем сборку образа

```
docker build -t blog .
```

Теперь нужно запустить контейнер

```
docker run --name blog -it -p 8000:8000 blog
```

### Автор разработки:
[Владислав Тутункин](https://github.com/TutunkinVladislav)
