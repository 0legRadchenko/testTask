# REST API (GeoDjango, Celery)
* Помимо CRUD и базовых задач реализованы 2 дополнительных задания:
1) Обновление/актуализация данных по cron из внешних источников (каждые 30 секунд)
2) Возможность фильтрации списка компаний по расстоянию (в порядке относительно наименьшей близости) от текущего местоположения пользователя.


## Инструкция по установке

* git clone https://github.com/0legRadchenko/testTask.git
##### После клонирования, ПРИ БОЛЬШОМ ЖЕЛАНИИ, можно заменить автосгенерированные: базу данных, пользователя, пароль к пользователю в POSTGRESQL на свои собственные в файлах:
1) settings.py - DATABASES: NAME, USER, PASSWORD
2) docker-compose-yml - db - environment: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
3) .env.dev - DEBUG (установить 1 или 0)

##### Собираем docker-compose
* docker-compose up --build -d
##### Делаем обязательные миграции
docker exec -it spider_group_web_1 python manage.py migrate
##### Создаем суперпользователя (админа)
docker exec -it spider_group_web_1 python manage.py createsuperuser
##### Смотрим логи celery (если интересно посмотреть)
* docker logs spider_group_celery_1
##### Проводим тесты
* docker exec -it spider_group_web_1 python manage.py test
## Инструкция по эксплуатации (базовое описание - подробности смотреть в swagger)
* Для общего представления о сервисе внедрен swagger: http://127.0.0.1:8000/swagger/
##### Пользователь:
* Создать пользователя: GET {'username': 'ИМЯ', 'password': 'ПАРОЛЬ'}
* Обновить пользователя: PUT {'user_location': {'latitude': 45.052409872249356, 'longitude': 39.03}, 'phone': '89005353535'} (больше ключей смотреть в swagger)


### Общий шаблон у категорий/компаний/продуктов (на примере компаний)
* GET http://127.0.0.1:8000/api/main/companies/
* GET http://127.0.0.1:8000/api/main/companies/1/
* POST http://127.0.0.1:8000/api/main/companies/ {'location': '{'latitude': 44.052409872249356, 'longitude': 39.03}', 'name': 'name', 'description': 'description'} 
* PUT http://127.0.0.1:8000/api/main/companies/1/ {'location': '{'latitude': 44.052409872249356, 'longitude': 39.03}', 'name': 'name', 'description': 'description'}
* DELETE http://127.0.0.1:8000/api/main/companies/1/
* То же самое с categories: api/main/categories/ и api/main/products/
##### Компании:
* Фильтрация компаний по локациям доступна только при ЗАДАННОЙ ГЕОЛОКАЦИИ У ПОЛЬЗОВАТЕЛЯ. Фильтрация идет от ближайших (известных локаций, если они присутствуют у компаний) до неизвестных (т.е отсутствующих None).
* Локация пользователя отправляется в виде json словаря вида: {'latitude': 44.05240, 'longitude': 39.03}
### Пример работы celery (получение данных из внешних api)
* Данные обновляются каждые 30 секунд
* Обновляются и добавляются категории, компании и продукты к ним







