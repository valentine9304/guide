# Справочник организации

Небольшой сервис на Python, который будет хранить в себе информацию об организациях.

Для удобства работы с проектом развернут Swagger [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Установка

1. Клонируйте репозиторий:
```
git clone git@github.com:valentine9304/guide.git
```
2. Запускаем PostgresSQL
3. Создайте .env файл по типу env_example
4. Устанавливаем виртуальное окружение, активируем его
```
  python -m venv venv 
  source venv/Scripts/activate  ( WINDOWS)
  . venv/bin/activate (LINUX)
```
5. Устаналиваем зависимоти pip install -r requirements.txt
6. Делаем миграцию и записываем рандомные данные в базу
```
alembic revision --autogenerate -m "create tables"
alembic upgrade head
python seed.py
```
7. Запускаем Fast API локально
```
uvicorn src.main:app --reload
```
8. Заходим по адресу [http://localhost:8000](http://localhost:8000)

Либо запускаем через Docker:

2. Заходим в директорию с проектом
3. Разверните приложение через docker
```
docker-compose up --build
```
4. Заходим по адресу [http://localhost:8000](http://localhost:8000)


## Автор
:trollface: Валентин :sunglasses:  
