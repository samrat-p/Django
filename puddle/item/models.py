from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model): 
    name = models.CharField(max_length=255) #defining name here

    class Meta:
        ordering =('name',)
        verbose_name_plural = 'Categories' #changing categorys to category

    def __str__(self):
        return self.name #categories item 1,2 was showing for fixing this so that the function would return its own defined name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.TextField(blank=True, null=True) #defining name here
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    is_sold = models.BooleanField(default=False) #defining
    created_at = models.DateTimeField(auto_now_add=True) #defining created_at
    created_by = models.ForeignKey(User,related_name='items' ,on_delete=models.CASCADE) #defining created_by and On_delete=CASCADE means when a user is deleted all items are deleted which had been created by user before
    image = models.ImageField(upload_to='item_images',blank=True, null=True) #defining image
    
    def __str__(self):
        return self.name


