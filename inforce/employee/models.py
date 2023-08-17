from django.db import models
from django.contrib.auth.models import User

from restaurant.models import Menu

# Create your models here.
class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)