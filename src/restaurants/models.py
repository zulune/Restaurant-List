from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save

from django.core.urlresolvers import reverse
from django.conf import settings

from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL
# Create your models here.
class RestaurantQuerySet(models.query.QuerySet):
    def search(self, query):
        if query:
            print(query)
            return self.filter(
                Q(name__icontains=query)|
                Q(location__icontains=query)|
                Q(location__iexact=query)|
                Q(category__icontains=query)|
                Q(category__iexact=query)|
                Q(item__name__icontains=query)|
                Q(item__contents__icontains=query)
            ).distinct()
        return self


class RestaurantManager(models.Manager):
    def get_queryset(self):
        return RestaurantQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class Restaurant(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, blank=True, null=True)
    category = models.CharField(max_length=120, blank=True, null=True, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    objects = RestaurantManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("restaurants:detail", kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print("Saved....!!")
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()

pre_save.connect(rl_pre_save_receiver, sender=Restaurant)

# post_save.connect(rl_post_save_receiver, sender=Restaurant)
