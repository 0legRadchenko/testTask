from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Product)
