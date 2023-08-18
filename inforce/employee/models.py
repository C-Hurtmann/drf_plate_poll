from django.db import models
from django.conf import settings
from django.utils import timezone

from restaurant.models import Menu


# Create your models here.
class Vote(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["create_date", "user"], name="Vote of user on date"
            )
        ]

    @classmethod
    def get_today_votes(cls):
        today = timezone.now().date()
        return cls.objects.filter(create_date__date=today)
