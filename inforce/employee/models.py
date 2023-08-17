from django.db import models
from django.conf import settings

from restaurant.models import Menu

# Create your models here.
class Vote(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)