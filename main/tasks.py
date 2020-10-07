from datetime import timedelta
from celery.task import periodic_task
from time import sleep
from django.conf import settings
import requests
from main.models import *
from django.db import connections
from django.db.migrations.recorder import MigrationRecorder

@periodic_task(run_every=timedelta(seconds=30))
def func():
    recorder = MigrationRecorder(connections['default'])
    migrations_were_applied = recorder.applied_migrations()
    print("\033[0m"+'#####################', migrations_were_applied)
    if migrations_were_applied:
        session = requests.Session()
        url = 'http://otp.spider.ru/test/companies/'
        r = session.get(url, headers={'Content-Type': 'application/json'})
        r = r.json()
        for d in r:
            i = d['id']
            name = d['name']
            if d.get('description'):
                description = d['description']
            else:
                description = ''

            COMPANY, _ = Company.objects.update_or_create(
                name=name, defaults={'name': name, 'description': description}
            )

            products_url = f'http://otp.spider.ru/test/companies/{i}/products/'
            result = session.get(products_url, headers={'Content-Type': 'application/json'})
            fetched_data_of_company = result.json()

            for d in fetched_data_of_company:
                category = d.get('category')
                category_name = category.get('name')

                CATEGORY, _ = Category.objects.update_or_create(
                    title=category_name, defaults={'title': category_name}
                )
                product_name = d.get('name')
                description = d.get('description')
                description = '' if description is None else description

                print(Product.objects.update_or_create(
                    title=product_name, description=description, defaults={'title': product_name,
                                                 'description': description,
                                                 'category': CATEGORY,
                                                 'company': COMPANY}
                ))
    else:
        print("\033[91m"+'PLEASE MAKE MIGRATIONS: docker exec -it spider_group_web_1 python manage.py migrate')