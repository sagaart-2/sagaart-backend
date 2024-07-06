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

Проект можно посмотреть по адресу: 
http://158.160.142.238/api/v1/
https://sagaart-market.vercel.app/

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

## Тесты и покрытие

Запустите тесты из корневой директории командой:

  ```
    python manage.py test apps
  ```
  или
  ```
    coverage run --source='.' manage.py test apps
  ```

Покрытие тестами составляет 83 процента.

![Процент покрытия](coverage.png)

## Команда разработки:

### Проджект-менеджер

*Лисицын Антон*  
**telegram:** [*@antony_lis*](https://t.me/antony_lis)  
**github:** [*Lisitsyn-AV*](https://github.com/Lisitsyn-AV) 

### Продакт-менеджер

*Акопян Погос*  
**telegram:** [*@pogo_s*](https://t.me/pogo_s)  
**github:** [*pogos-akopian* ](https://github.com/pogos-akopian)  

### UX/UI дизайнеры

*Гапонов Виктор*  
**telegram:** [*@way26ru*](https://t.me/way26ru)  
**github:** [*Vik*](https://github.com/Vik)  

*Ерёменко Татьяна*  
**telegram:** [*@paintings_inspire*](https://t.me/paintings_inspire)  

### Бизнес-аналитики

*Гаврилова Анастасия*  
**telegram:** [*@Tarasovna*](https://t.me/Tarasovna)  
**github:** [*Nastya-Gavrilova*](https://github.com/Nastya-Gavrilova)  

*Гахраманова Айна*  
**telegram:** [*@fghtyvb*](https://t.me/fghtyvb)  
**github:** [*aynaitsme*](https://github.com/aynaitsme)  

### Системные аналитики

*Селиванова Ольга*  
**telegram:** [*@Lelia7*](https://t.me/Lelia7)  
**github:** [*Olga9221555515*](https://github.com/Olga9221555515)  

*Дергунова Мария*  
**telegram:** [*@Dergunovamv*](https://t.me/Dergunovamv)  
**github:** [*marderg*](https://github.com/marderg)  

*Лыков Илья*  
**telegram:** [*@ilia_likov*](https://t.me/ilia_likov)  
**github:** [*ilia.likov*](https://github.com/ilia.likov)  

*Мазитов Роберт*  
**telegram:** [*@Mazitov47*](https://t.me/Mazitov47)  
**github:** [*RobMaz47*](https://github.com/RobMaz47)  

### Frontend-разработчики

*Парада Елизавета*  
**telegram:** [*@ElizavetaParada*](https://t.me/ElizavetaParada)  
**github:** [*Elizaveta-Parada*](https://github.com/Elizaveta-Parada)  

*Мильне Ольга*  
**telegram:** [*@helgamilne*](https://t.me/helgamilne)  
**github:** [*HelgaMilne*](https://github.com/HelgaMilne)  

### Backend-разработчики

*Васин Никита*  
**telegram:** [*@cskovec22*](https://t.me/cskovec22)  
**github:** [*cskovec22*](https://github.com/cskovec22)  

*Лашков Павел*  
**telegram:** [*@hutjinator*](https://t.me/hutjinator)  
**github:** [*hutji*](https://github.com/hutji)  

### QA-инженер

*Найгум Алексей*  
**telegram:** [*@alekseynaigum*](https://t.me/alekseynaigum)  
**github:** [*AlekseyNaigum*](https://github.com/AlekseyNaigum)  
