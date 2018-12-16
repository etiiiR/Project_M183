# Create your models here.
import datetime
import logging

import django.core.validators
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


logger = logging.getLogger(__name__)



class Antrag(models.Model):
    Vorname = models.CharField(max_length=60)
    Nachname = models.CharField(max_length=60)
    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        
    )

    Antragswunsch = models.CharField(max_length=60)
    Kontotyp = models.CharField(max_length=60)


class Bankaccoount(models.Model):
    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        
    )

    Money = models.IntegerField(default=1)
    date = models.DateField(("Date"), default=datetime.date.today)
    
    class Meta:
        permissions = (
            ("can_see_bankaccount", "View a bancaccount"),
            ("can_change_bankaccount", "Can change a bankaccount"),
            ("can_delete_bankaccount", "Can delete a bankaccount"),
            ("can_abheben", "Kann ein Abheben von einem Bankaccount"),
            ("can_einzahlen", "Kann ein Abheben von einem Bankaccount"),
            ("can_bankeröffnung", "Kann ein Bankacccount eröffnen"),
            ("can_payafriend", "Kann ein Geld an einen Freund senden")
        )
    def __str__(self):
        return 'Bankaccount: ' + str(self.User) + " " + str(self.id)


class Transaktion(models.Model):
    Money_to = models.ForeignKey(Bankaccoount, related_name="destination_account", on_delete=models.CASCADE)
    Value = models.PositiveIntegerField(default=1)
    Money_from = models.ForeignKey(Bankaccoount, related_name="source_account", on_delete=models.CASCADE )
    
    def __str__(self):
        return self.Money_from.User.username + " " + str(self.Money_from.id) +  " to " + self.Money_to.User.username + " " + str(self.Money_to.id)