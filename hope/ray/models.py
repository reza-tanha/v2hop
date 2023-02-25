from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Server(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=40
    )

    username = models.CharField(
        verbose_name="username xui panel",
        max_length=40,
        default="None",
        null=True,
        blank=True

    )

    password = models.CharField(
        verbose_name="password xui panel",
        max_length=40,
        default="None",
        null=True,
        blank=True
    )
    ip = models.CharField(
        max_length=40,
        verbose_name="ip Server"
    )

    domain_country = models.CharField(
        verbose_name="Domain Name",
        # unique=True,
        max_length=5
    )

    down = models.BooleanField(
        default=False,
        verbose_name="Down"
    )

    def __str__(self) -> str:
        return self.name


class ConfigVpn(models.Model):

    conf = models.TextField(
        verbose_name="HashV2ray",
        unique=True
    )

    uuid = models.TextField(
        verbose_name="uuid",
        null=True,
        blank=True
    )

    server = models.ForeignKey(
        to=Server,
        on_delete=models.SET_NULL,
        related_name="server_configvpn",
        verbose_name="server",
        null=True,
        blank=True
    )

    volume = models.IntegerField(
        verbose_name="Volume : MB",
        default=150
    )

    is_tunel = models.BooleanField(
        default=False,
        verbose_name="Is Tunel ?"
    )

    expire_date = models.DateField(
        verbose_name="Expire Date Time",

        null=True,
        blank=True
    )

    user = models.ForeignKey(
        to=User,
        verbose_name="User",
        related_name="user_configvpn",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    is_use = models.BooleanField(
        verbose_name="Is Use This Config?",
        default=False
    )

    def __str__(self) -> str:
        return f"{self.server.name} : {str(self.volume)}"


class Subscribe(models.Model):

    price = models.IntegerField(
        verbose_name="Price : Rial"
    )

    volume = models.IntegerField(
        verbose_name="Volume : MB",
        default=10240
    )

    def __str__(self) -> str:
        return f"تومان {int(self.price / 10) :,} : GB {int(self.volume / 1024)}"
