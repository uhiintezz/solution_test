<h2 align="center">Веб-сервис для управления движением денежных
средств (ДДС)</h2>


**Ссылка**:
- [solutiontest.ru]([https://](https://solutiontest.ru/))


### Описание проекта:
В приложении пользователь имеет возможность вести учет денежных операций. Возможность добавлять, удалять, редактировать записи.
Каждая запись имеет статус тип, категорию, подкатегории. В пункте меню "Управление справочниками" можно управлять параметрами записи.
В главном меню есть фильтрация по дате, статусу, типу, категории и подкатегории. 


### Инструменты разработки

**Стек:**
- Python >= 3.10
- Django == 4.1.3
- mysqlclient == 2.2.0
- djangorestframework == 3.14.0
- django-filter == 22.1
- Bootstrap
- JavaScript

## Инструкция по запуску


##### 1) Клонировать репозиторий

    git clone https://github.com/uhiintezz/solution_test.git

##### 2) Создать виртуальное окружение

    cd solution_test
    
    python -m venv djangoenv
    
##### 3) Активировать виртуальное окружение
    
Linux

    source djangoenv/bin/activate
    
Windows

    ./djangoenv/Scripts/activate

##### 5) Устанавливать зависимости:

    pip install -r requirements.txt

##### 6) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 8) Создать суперпользователя

    python manage.py createsuperuser
    
##### 9) Запустить сервер

    python manage.py runserver
#### 10) 
    приложение будет доступно в браузере по 127.0.0.1:8000

