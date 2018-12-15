# Create your models here.
from django.db import models
from django.conf import settings
import datetime
import logging

logger = logging.getLogger(__name__)


class Bankaccoount(models.Model):
    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        
    )

    Money = models.IntegerField(default=1)
    def __str__(self):
        return self.Money
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
        
logger.info("Bankaccount wurde im Backend eröffnet %s", Bankaccoount.User)