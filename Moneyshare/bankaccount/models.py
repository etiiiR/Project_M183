# Create your models here.
from django.db import models
from django.conf import settings


class Bankaccoount(models.Model):
    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    Money = models.IntegerField(default=1)
