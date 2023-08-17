from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1)
    day_of_week = models.SmallIntegerField()
    dishes = models.ManyToManyField(Dish)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['restaurant', 'day_of_week'], name='Weekday menu for restaurant')
        ]
