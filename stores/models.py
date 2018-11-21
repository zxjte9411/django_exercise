from django.db import models

# Create your models here.

class Store(models.Model):

    name = models.CharField(max_length=20)
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    store = models.ForeignKey('Store', on_delete=models.CASCADE,related_name='menu_items')
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name