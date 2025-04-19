# Lalasia API

API для работы оплаты на проекте для [курса по React от KTS](https://github.com/dmhd6219-additional-projects/kts-react-project), написанный на python

## Запуск локально через Docker

### 1. Клонирование репозитория

   ```
   git clone https://github.com/dmhd6219-additional-projects/kts-react-project-backend
   cd kts-react-project-backend
   ```

### 2. Сборка Docker образа

```
docker build -t dmhd6219/react-project-backend:latest -f Dockerfile .
```

### 2. Получение API ключей

   Для получения API ключей нужно
   следовать [данной инструкции](https://yookassa.ru/docs/support/merchant/payments/implement/test-store).
   Нужно зарегистрироваться в ЮКасса, затем создать тестовый магазин. В ЛК в шапке будет id магазина в формате
   `shopId<нужный числовой id>`.
   Затем через боковое меню нужно перейти в раздел "интеграции", там в "ключи API". Там будет секретный ключ.

### 3. Создание `.env` файла

   В корне проекта нужно создать `.env` файл с форматом из [.env.example](.env.example) и с данными, полученными во
   втором пункте.

   Например:
   ```
    YOO_SECRET=test_-6asdDl2EuFAPCdsafdsfflmsdafsklC54gfgD7p9zdJSh0Xp7Jmjc
    YOO_APP_ID=3459328
   ```

### 4. Запуск проекта

```
docker run -d -p 8000:8000 --name react-project-backend-container --env-file .env dmhd6219/react-project-backend:latest
```