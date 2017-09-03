from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse

from restaurants.models import Restaurant
# Create your models here.

class Item(models.Model):
    # associations
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant  = models.ForeignKey(Restaurant)
    # item stuff
    name        = models.CharField(max_length=100)
    contents    = models.TextField(help_text='Separate each item by comma')
    excludes    = models.TextField(
        blank=True, null=True, help_text='Separate each item by comma'
    )
    public      = models.BooleanField(default=True)
    # date
    timestamp   = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-update", "-timestamp"]

    def __str__(self):
        return self.name    

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'pk': self.pk})
