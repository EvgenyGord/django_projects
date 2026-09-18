# 🐍 Django Projects

> Коллекция учебных проектов на Django: web-разработка, ORM, формы, шаблоны, CRUD, PostgreSQL/SQLite, связи моделей и работа с данными.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)](https://www.djangoproject.com/)
[![Database](https://img.shields.io/badge/Database-SQLite%20%7C%20PostgreSQL-336791?logo=postgresql)](https://www.postgresql.org/)

## 📌 О проекте

Репозиторий объединяет несколько небольших Django-приложений, созданных для практики Python backend и web-разработки.

Проекты покрывают разные аспекты Django:

- архитектура Django project/app;
- URL routing;
- views;
- templates;
- static files;
- Django ORM;
- ModelForm;
- CRUD;
- migrations;
- relationships;
- authentication;
- загрузка файлов;
- работа с PostgreSQL;
- SQLite для локальных приложений;
- пользовательские template tags и converters.

Это не один монолитный продукт, а **коллекция практических работ**, каждая из которых показывает отдельную технологию или концепцию Django.

---

## 🗂️ Состав репозитория

```text
django_projects/
│
├── bd_evgeny/
│   └── biblioteka/
│
├── form_project/
│   ├── feedback/
│   └── gallery/
│
├── movie_proj/
│   └── movie_app/
│
├── my_page/
│   ├── horoscope/
│   └── week_days/
│
├── my_site/
│   ├── blog/
│   └── geometry/
│
└── Evgeny/
    └── blog/
```

---

# 📚 Проекты

## 1. `bd_evgeny` — система управления библиотекой

Один из наиболее функциональных проектов коллекции.

### Основные сущности

```text
Author
   │
   └── Book
         │
         └── BookDistribution
                ├── Subscriber
                └── Employee

Genre ───────────┘
```

В приложении реализованы модели:

- `Author`
- `Employee`
- `Subscriber`
- `Genre`
- `Book`
- `BookDistribution`

### Возможности

- просмотр сущностей;
- добавление записей;
- редактирование;
- отчётные страницы;
- работа со связанными объектами;
- формы Django;
- авторизация;
- шаблоны для разных разделов;
- ORM;
- PostgreSQL.

### Структура

```text
bd_evgeny/
├── bd_evgeny/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── biblioteka/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   ├── templates/
│   └── static/
│
└── manage.py
```

---

## 2. `form_project` — формы и загрузка файлов

Проект демонстрирует работу Django Forms и Media Files.

### `feedback`

Модель обратной связи содержит:

- имя;
- фамилию;
- текст отзыва;
- рейтинг.

Используется `ModelForm` и валидация полей.

### `gallery`

Простая галерея с загрузкой файлов через:

```python
models.FileField(upload_to='my_gallery')
```

Практикуются:

- формы;
- обработка POST;
- templates;
- media files;
- модели;
- migrations.

---

## 3. `movie_proj` — каталог фильмов

Проект показывает работу Django ORM и связей между моделями.

### Модели

```text
Director
   │
   └──── Movie ─────┐
                    │
Actor ──────────────┘
   │
   └── DressingRoom

Student
```

### Используемые возможности Django

- ForeignKey;
- ManyToManyField;
- OneToOneField;
- choices;
- validators;
- slug;
- `reverse()`;
- detail pages;
- migrations;
- CRUD-oriented views.

Например, для рейтинга фильма используются ограничения:

```python
MinValueValidator(1)
MaxValueValidator(100)
```

---

## 4. `my_page` — страницы и horoscope

Набор небольших упражнений по Django routing, views и templates.

### `horoscope`

Реализована работа со знаками зодиака:

- список знаков;
- получение информации по имени;
- получение знака по порядковому номеру;
- redirects;
- custom converter;
- template tags;
- CSS.

### `week_days`

Небольшое приложение для практики URL-маршрутизации и views.

---

## 5. `my_site` — набор web-примеров

Содержит несколько независимых приложений.

### `blog`

Практика:

- templates;
- context;
- dynamic URL parameters;
- несколько представлений;
- передача данных в шаблоны.

### `geometry`

Небольшой пример обработки данных через Django views для геометрических фигур.

---

## 6. `Evgeny` — простой Django blog

Небольшой проект для практики:

- project/app structure;
- views;
- templates;
- static files;
- URL routing;
- базовая работа с Django.

---

# 🧠 Что демонстрирует репозиторий

| Область | Практика |
|---|---|
| Python | функции, структуры данных, ООП |
| Django | project/app architecture |
| Views | обработка HTTP-запросов |
| Templates | HTML + Django Template Language |
| ORM | модели и запросы |
| Forms | ModelForm / validation |
| CRUD | создание, просмотр, изменение данных |
| Relationships | FK / M2M / OneToOne |
| Routing | static и dynamic URLs |
| Auth | Django authentication |
| Files | upload / media |
| Migrations | изменение структуры БД |
| Databases | SQLite / PostgreSQL |
| Static | CSS и static files |

---

# ▶️ Как запустить отдельный проект

Каждая директория является отдельным Django-проектом и запускается из своей директории, где находится `manage.py`.

Например:

```bash
cd bd_evgeny
python manage.py runserver
```

После запуска:

```text
http://127.0.0.1:8000/
```

Для другого проекта:

```bash
cd movie_proj
python manage.py runserver
```

---

# 🛠️ Установка Django

Создание virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Установка Django:

```bash
pip install django
```

Для проекта с PostgreSQL также требуется соответствующий PostgreSQL driver.

---

# 🔍 Архитектурный подход

Большинство приложений построено вокруг классической структуры Django:

```text
Browser
   │
   ▼
urls.py
   │
   ▼
views.py
   │
   ├──────────────► templates/
   │
   ▼
models.py
   │
   ▼
Database
```

Формы добавляют отдельный слой обработки пользовательского ввода:

```text
User
 ↓
Form / ModelForm
 ↓
Validation
 ↓
View
 ↓
Model / ORM
 ↓
Database
```

---

# 🎓 Цель коллекции

Проекты создавались как практическая база для изучения Python/Django и понимания backend-части web-приложений.

Особенно полезно рассматривать репозиторий не как законченный production-продукт, а как **историю обучения и накопления практики**:

```text
Python
  ↓
Django basics
  ↓
Routing + Views
  ↓
Templates
  ↓
ORM
  ↓
Forms
  ↓
CRUD
  ↓
Relationships
  ↓
Databases
```

---


## 👨‍💻 About

**Python / QA Automation Engineer**

Этот репозиторий показывает практику работы с backend-частью Python-стека и является базой для дальнейшего развития в сторону **FullStack QA / QA Automation Engineering**.
