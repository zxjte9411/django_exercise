from django.db import models
from django.urls import reverse


class Store(models.Model):

    name = models.CharField(max_length=20)
    notes = models.TextField(blank=True, default='')

    def get_absolute_url(self):
        return reverse('stores:store_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    store = models.ForeignKey('Store', on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name
