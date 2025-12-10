# Лабораторная работа 5 - REST API для управления пользователями

## Технологии
- Python 3.12.8
- Litestar
- SQLAlchemy + SQLite
- Pydantic
- Docker
- UV (менеджер зависимостей)
- Linters: pre-commit, black, isort, pylint


## Установка и запуск через Docker

### 1. Клонируйте репозиторий
```bash
git clone <url-репозитория>
cd lab5
```

### 2. Соберите и запустите контейнер
```bash
docker build -t lab5-app .
docker run --rm -p 8000:8000 lab5-app
```

## Установка и запуск для разработки и проверки линтеров
### 1. Клонирование и настройка окружения
```bash
# Клонируйте репозиторий
git clone <url-репозитория>
cd lab3

# Установите UV (если не установлен)
pip install uv

# Установите зависимости через UV
uv sync
```
### 2. Заполнение БД
```bash
uv run python scripts/load_data.py
uv run python scripts/update_data.py
```

### 3. Запуск приложения
```bash
uv run python main.py
```

### 4. Проверка линтеров

#### Установите pre-commit хуки для автоматической проверки линтеров
```bash
pre-commit install
```

#### Ручной запуск всех проверок:
```bash
pre-commit run --all-files
```


## Команды для командной строки
### Вывод пользователей
```bash
curl "http://localhost:8000/users"
```

### Добавление пользователя
```bash
curl -X POST "http://localhost:8000/users" -H "Content-Type: application/json" -d "{\"username\":\"newuser\",\"email\":\"newuser@university.ru\"}"
```

### Вывод пользователя по ID
```bash
curl "http://localhost:8000/users/3"
```

### Изменение информации о пользователе
```bash
curl -X PUT "http://localhost:8000/users/3" -H "Content-Type: application/json" -d "{\"email\":\"updated@university.ru\"}"
```

### Удаление информации о пользователе
```bash
curl -X DELETE "http://localhost:8000/users/3"
```

### Получение информации по фильтру
```bash
curl "http://localhost:8000/users?username=kozlov"
```

## Тестирование

### 1. Запуск всех тестов
```bash
pytest
```
### 2. Запуск unit-тестов
#### Репозитории
```bash
pytest tests/test_repositories
```

#### Сервисы
```bash
pytest tests/test_services
```

#### API-ендпоинты
```bash
pytest tests/test_controllers
```

### 3. Отчет о покрытии
```bash
pytest --cov-report=html
```