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

    is_send_ads = models.BooleanField(
        default=False,
        verbose_name="send ads status"
    )

    send_ads_time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="send ads time"
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

    balance = models.BigIntegerField(
        default=0,
        verbose_name="Balance"
    )

    test_date = models.DateTimeField(
        default=None,
        null=True,
        blank=True
    )

    wallat = models.CharField(
        max_length=40,
        verbose_name="Usser Wallat",
        unique=True,
        default=None,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f"{str(self.user)}"
