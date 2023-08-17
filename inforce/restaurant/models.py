from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f'{self.name}'


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return f'{self.name}'

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=1)
    day_of_week = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    dishes = models.ManyToManyField(Dish)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['restaurant', 'day_of_week'], name='Weekday menu for restaurant')
        ]
    
    def __str__(self):
        return f'{self.restaurant} on {self.day_of_week}'