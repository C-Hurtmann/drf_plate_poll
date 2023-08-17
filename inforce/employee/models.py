from django.db import models
from django.conf import settings

from restaurant.models import Menu

# Create your models here.
class Vote(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['create_date', 'user'], name='Vote of user on date')
        ]