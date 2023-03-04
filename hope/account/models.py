from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    user_id = models.IntegerField(
        unique=True,
        verbose_name="UserId"
    )

    step = models.CharField(
        max_length=30,
        verbose_name="Step",
        default="home"
    )

    is_sent_ads = models.BooleanField(
        default=False,
        verbose_name="Did the ads message get sent?"
    )

    sent_ads_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Sent message time"
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['user_id']

    def __str__(self):
        return str(self.user_id)


class Balance(models.Model):

    user = models.OneToOneField(
        to=User,
        on_delete=models.SET_NULL,
        verbose_name="Account Balance",
        related_name="user_balance",
        null=True,
        blank=True
    )

    balance = models.IntegerField(
        default=0,
        verbose_name="Balance"
    )

    test_date = models.DateTimeField(
        default=None,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{str(self.user.user_id)} : {self.user.first_name}"
