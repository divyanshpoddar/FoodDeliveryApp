from django.db import models
from datetime import datetime


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='_menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('MenuItem', related_name='order')
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    hostel = models.CharField(max_length=10, blank=True)
    block = models.IntegerField(blank=True, null=True)
    room = models.CharField(max_length=10, blank=True)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'OrderModels: {self.created_on.strftime("%b %d %I: %M %p")}'
