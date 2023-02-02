from django.contrib import admin

# Register your models here.
from .models import Category,Item

admin.site.register(Category)  #categories.register
admin.site.register(Item) #items.register