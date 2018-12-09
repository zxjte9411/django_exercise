from django.conf import settings
from django.urls import reverse
from django.db import models

from stores.models import MenuItem, Store


class Event(models.Model):

    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return str(self.store)

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'pk': self.pk})


class Order(models.Model):

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='orders')
    item = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, related_name='orders')
    notes = models.TextField(blank=True, default='')

    # Django 用來提示某個 class 應該擁有什麼屬性的工具。以 model form 而言，在 meta 中指定 model 屬性
    class Meta:
        unique_together = ('event', 'user',)

    def __str__(self):
        return '{item} of {user} for {event}'.format(item=self.item, user=self.user, event=self.event)
