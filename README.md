# REST API (GeoDjango, Celery)
* Помимо CRUD и базовых задач реализованы 2 дополнительных задания:
1) Обновление/актуализация данных по cron из внешних источников (каждые 60 секунд)
2) Возможность фильтрации списка компаний по расстоянию (в порядке относительно наименьшей близости) от текущего местоположения пользователя.


## Инструкция по установке

* git clone https://github.com/0legRadchenko/testTask.git
##### После клонирования, при желании, можно заменить автосгенерированные базу данных/пользователя/пароль к пользователю) в POSTGRESQL и заменить данные на свои в файлах:
1) settings.py - DATABASES: NAME, USER, PASSWORD
2) docker-compose-yml - db - environment: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
3) .env.dev - DEBUG (установить 1 или 0)

##### Собираем docker-compose
* docker-compose up --build -d
##### Делаем обязательные миграции
docker exec -it spider_group_web_1 python manage.py migrate
##### Смотрим логи celery (если интересно посмотреть)
* docker logs spider_group_celery_1
##### Проводим тесты
* docker exec -it spider_group_web_1 python manage.py test







