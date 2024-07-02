# Проект "SAGAART"

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=008080)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=008080)](https://github.com/features/actions)

## Описание проекта "SAGAART"

Проект «SAGAART» — онлайн-платформа для расчета
стоимости и продажи арт-объектов. API позволяет просматривать список пользователей, добавлять карточки товара и опубликовывать информацию по событиям для галерей.

Проект можно посмотреть по адресу: http://158.160.142.238/api/v1/

## Запуск проекта локально

- Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone git@github.com:sagaart-2/sagaart-backend.git
cd sagaart-backend
```

- Установите и активируйте виртуальное окружение:

```
python -m venv venv
```

- Для Linux/macOS:

    ```
    source venv/bin/activate
    ```

- Для Windows:

    ```
    source venv/Scripts/activate
    ```

- Установите зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Создайте файл .env в папке проекта, пример представлен в файле .env-example-local


- Перейдите в папку с файлом manage.py


- Примените миграции:
```
python manage.py makemigrations
python manage.py migrate
```

- Соберите статику:
```
python manage.py collectstatic
```

- Создайте суперпользователя:
```
python manage.py createsuperuser
```

- Запустите проект:
```
python manage.py runserver
```

- Документацию можно посмотреть по адресу:
```
http://127.0.0.1:8000/swagger/
```

## Запуск в контейнерах

Запустите контейнеры следующей командой:
  ```
    docker compose up -d
  ```

Выполните миграции:
  ```
    docker compose exec backend python manage.py makemigrations
    docker compose exec backend python manage.py migrate
  ```

Создайте суперпользователя:
  ```
    docker compose exec backend python manage.py createsuperuser
  ```

Зайти в админ-панель:
[Admin](http://127.0.0.1:8000/admin/)

Посмотреть документацию:
[Swagger](http://127.0.0.1:8000/swagger/)

## CI/CD
### Описание и настройка

- при пуше в любую ветку запускаются тесты
- при мёрдже PR в ветки `develop` проект запускается на удалённом сервере

Для корректной работы CI/CD необходимо создать секретные переменные репозитория
(Repository secrets):
```text
DOCKER_USERNAME=<docker_username>
DOCKER_PASSWORD=<docker_password>

SERVER_HOST=<server_pub_ip>
SERVER_USER=<username>

SSH_KEY=<--BEGIN OPENSSH PRIVATE KEY--...--END OPENSSH PRIVATE KEY--> # cat ~/.ssh/id_rsa
SSH_PASSPHRASE=<ssh key passphrase>
```

## Список эндпоинтов API:

- /api/v1/users/ - список пользователей
- /api/v1/users/{id}/ - получение, изменение или удаление пользователя
- /api/v1/artists/ - создание художника
- /api/v1/artists/{id}/ - получение, изменение или удаление художника
- /api/v1/product_cards/ - список карточек товаров или создание карточки товара
- /api/v1/product_cards/{id}/ - получение, изменение или удаление карточки товара
- /api/v1/styles/ - список стилей
- /api/v1/styles/{id}/ - получение или удаление стиля
- /api/v1/categories/ - список категорий
- /api/v1/categories/{id}/ - получение или удаление категории
- /api/v1/orders/ - список заказов или создание заказа
- /api/v1/orders/{id}/ - получение или удаление заказа
- /api/v1/bids/ - создание заявки на определение цены картины
- /api/v1/bids/{id}/ - получение заявки на определение цены картины

Подробную информацию по эндпоинтам API можно посмотреть по адресу:
```
http://158.160.142.238/swagger/
```

## Команда разработки:

### Проджект-менеджер

*Лисицын Антон*
**telegram:** *@antony_lis*
**github:** *Lisitsyn-AV*

### Продакт-менеджер

*Акопян Погос*
**telegram:** *@pogo_s*
**github:** *pogos-akopian*

### UX/UI дизайнеры

*Гапонов Виктор*
**telegram:** *@way26ru*
**github:** *Vik*

*Ерёменко Татьяна*
**telegram:** *@paintings_inspire*

### Бизнес-аналитики

*Гаврилова Анастасия*
**telegram:** *@Tarasovna*
**github:** *Nastya-Gavrilova*

*Гахраманова Айна*
**telegram:** *@fghtyvb*
**github:** *aynaitsme*

### Системные аналитики

*Селиванова Ольга*
**telegram:** *@Lelia7*
**github:** *Olga9221555515*

*Дергунова Мария*
**telegram:** *@Dergunovamv*
**github:** *marderg*

*Лыков Илья*
**telegram:** *@ilia_likov*
**github:** *ilia.likov*

*Мазитов Роберт*
**telegram:** *@Mazitov47*
**github:** *RobMaz47*

### Frontend-разработчики

*Парада Елизавета*
**telegram:** *@ElizavetaParada*
**github:** *Elizaveta-Parada*

*Мильне Ольга*
**telegram:** *@helgamilne*
**github:** *HelgaMilne*

### Backend-разработчики

*Васин Никита*
**telegram:** *@cskovec22*
**github:** *cskovec22*

*Лашков Павел*
**telegram:** *@hutjinator*
**github:** *hutji*

### QA-инженер

*Найгум Алексей*
**telegram:** *@alekseynaigum*
**github:** *AlekseyNaigum*
