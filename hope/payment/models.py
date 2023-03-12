from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class SingletonModel(models.Model):
    def save(self, *args, **kwargs):
        self.id = 1
        return super().save(*args, **kwargs)


class Wallet(models.Model):

    name = models.CharField(
        max_length=20,
        verbose_name="Name : Tron"
    )

    wallet = models.CharField(
        max_length=90,
        verbose_name="Wallet",
        unique=True
    )

    def __str__(self):
        return f"{self.name} : {self.wallet}"


class ContractAddres(models.Model):

    symbol = models.CharField(
        max_length=15,
        verbose_name="Symbol : USDT, TRX, "
    )

    contract_addres = models.CharField(
        max_length=90,
        verbose_name="contract_addres",
        default=None,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f"{self.symbol}"


class UserPayments(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
        related_name="user_userpayment"
    )

    transaction_id = models.CharField(
        max_length=64,
        verbose_name="Transaction Id",
        unique=True
    )

    date = models.DateTimeField(
        auto_now=True
    )

    status = models.BooleanField(
        verbose_name="Status",
        default=False,
        null=True,
        blank=True
    )

    owner_address = models.CharField(
        max_length=64,
        verbose_name="ownerAddress",
        null=True,
        blank=True
    )

    amount = models.FloatField(
        verbose_name="amount",
        default=0,
        blank=True
    )

    contract_address = models.CharField(
        max_length=64,
        verbose_name="contract_address",
        default=None,
        null=True,
        blank=True
    )

    contract_ret = models.CharField(
        max_length=64,
        verbose_name="contractRet",
        default=None,
        null=True,
        blank=True
    )

    sr_confirm_list = models.IntegerField(
        verbose_name="srConfirmList",
        default=0,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.user.first_name} : {self.user.user_id}"


class BotUpdateStatus(SingletonModel):
    is_update = models.BooleanField(
        verbose_name="update status",
        default=True
    )

    def __str__(self):
        return f"Bot status is: {self.is_update}"
