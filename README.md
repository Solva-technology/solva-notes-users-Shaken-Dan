[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20996801&assignment_repo_type=AssignmentRepo)
# Note App — Часть #4: Пользователи и права доступа

## Цель  
Добавить систему пользователей в проект, реализовать регистрацию, авторизацию, восстановление пароля и ограничить доступ к заметкам: редактировать и удалять их может только автор или администратор.

---

## Описание проекта  
**Note App** — учебное Django-приложение для работы с заметками.  

Проект уже включает:  
- админку и локализацию;  
- список заметок (главная), страницу отдельной заметки, страницу редактирования / удаления заметки;  
- CRUD для модели Note через Django Forms;  
- базовый шаблон `base.html`;  
- запуск в Docker + PostgreSQL.  

На этом этапе необходимо расширить приложение за счет пользователей и разграничения прав доступа.  

---

## Новые возможности  

### 1. Регистрация пользователя  
- **URL**: `/auth/register/`  
- Форма регистрации с полями: `username`, `email`, `пароль` (дважды).  
- После успешной регистрации → автоматическая авторизация и редирект на главную.  

### 2. Авторизация и выход  
- **URL (login)**: `/auth/login/`  
- **URL (logout)**: `/auth/logout/`  
- После входа → редирект на главную.  
- После выхода → редирект на страницу авторизации.  

### 3. Восстановление пароля  
- Использовать встроенные Django views.  
- Должны быть доступны страницы:  
  - `/auth/password_reset/` — форма ввода email,  
  - `/auth/password_reset/done/`,  
  - `/auth/reset/<uidb64>/<token>/` — ввод нового пароля,  
  - `/auth/reset/done/`.  

### 4. Ограничение прав  
- Только автор заметки или администратор может редактировать/удалять заметку.  
- Если другой пользователь попытается перейти на страницу редактирования/удаления → отображается ошибка *«Доступ запрещен»*.  
- На уровне шаблонов: кнопки **«Редактировать»** и **«Удалить»** отображаются только автору и администратору.  

---

## Требования  
- Использовать встроенную модель пользователя `User` из Django.  
- Применять `django.contrib.auth` и стандартные views (`LoginView`, `LogoutView`, `PasswordResetView` и т.д.).  
- Все шаблоны должны наследоваться от `base.html`.  
- В шапке (`header`) должны быть ссылки: **«Регистрация»**, **«Войти/Выйти»**, **«Мои заметки»**.  
- При создании заметки поле `author` автоматически заполняется текущим пользователем.  

---

## Структура проекта (пример)  

```
note_app/
├── notes/
│   ├── templates/notes/
│   │   ├── note_form.html
│   │   ├── note_confirm_delete.html
│   │   ├── note_detail.html
│   │   └── note_list.html
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── users/
│   ├── templates/registration/
│   │   ├── login.html
│   │   ├── logout.html
│   │   ├── register.html
│   │   ├── password_reset_form.html
│   │   ├── password_reset_done.html
│   │   ├── password_reset_confirm.html
│   │   └── password_reset_complete.html
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── templates/base.html
├── docker-compose.yml
├── Dockerfile
└── .env.example
```
## Инструкция по запуску проекта

### Скачайте репозиторий
- git clone https://github.com/<your_username>/solva-notes-admin-Shaken-Dan.git

### Запустите Docker
- docker compose up --build

### Сделайте миграцию БД
- docker compose exec web python manage.py migrate

### Создайте пользователя (укажите имя и пароль)
- docker compose exec web python manage.py createsuperuser

### Загрузите фикстуры 
- docker compose exec web python manage.py loaddata initial_data.json 

### Главная страница: список всех заметок
- http://localhost:8000

### Регистрация нового пользователя
- http://127.0.0.1:8000/auth/register/

### Логин пользователя
- http://127.0.0.1:8000/auth/login/

### Пользователь после регистрации может изменить свой пароль
- http://127.0.0.1:8000/auth/password-reset

### Пользователь может создавать новые заметки и редактировать имеющиеся, чужие редактировать не может



#### Автор 
Shaken-Dan Bolatuly