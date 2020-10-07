from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Category(models.Model):
    title = models.CharField(verbose_name="Категория", max_length=150, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Company(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)
    description = models.TextField('Описание')
    is_active = models.BooleanField(default=True)
    location = models.PointField(srid=4326, geography=True, null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Product(models.Model):
    title = models.CharField('Заголовок', max_length=150, unique=True)
    description = models.TextField('Описание', blank=True)
    company = models.ForeignKey(Company,
                                verbose_name='Компания',
                                on_delete=models.CASCADE,
                                related_name="company_products")

    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 on_delete=models.CASCADE,
                                 related_name="products_of_this_category")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField('Имя', max_length=100, blank=True)
    last_name = models.CharField('Фамилия', max_length=100, blank=True)
    email = models.EmailField(max_length=70,blank=True)
    phone = models.TextField('Телефон', blank=True)
    user_location = models.PointField("Местоположение", srid=4326, geography=True, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Пользовательский профиль"
        verbose_name_plural = "Пользовательские профили"










