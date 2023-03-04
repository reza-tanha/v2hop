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

    is_tunnel = models.BooleanField(
        default=False,
        verbose_name="Is Tunnel ?"
    )

    def __str__(self) -> str:
        return self.name


class ProxyConfig(models.Model):

    user = models.ForeignKey(
        to=User,
        verbose_name="User",
        related_name="proxy_config",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    server = models.ForeignKey(
        to=Server,
        on_delete=models.SET_NULL,
        related_name="proxy_config",
        verbose_name="server",
        null=True,
        blank=True
    )

    proxy_hash = models.TextField(
        verbose_name="HashV2ray",
        unique=True
    )

    uuid = models.TextField(
        verbose_name="uuid",
        null=True,
        blank=True
    )

    volume = models.IntegerField(
        verbose_name="Volume : MB",
        default=150
    )

    last_num_change = models.IntegerField(
        verbose_name="Last Change Server",
        default=0
    )
    
    is_use = models.BooleanField(
        verbose_name="Is this configuration used?",
        default=False
    )
    
    expire_date = models.DateField(
        verbose_name="Expire Date Time",
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.server.name} : {str(self.volume)}"


class Plan(models.Model):

    price = models.IntegerField(
        verbose_name="Price : Rial"
    )

    volume = models.IntegerField(
        verbose_name="Volume : MB",
        default=10240
    )

    def __str__(self) -> str:
        return f"تومان {int(self.price / 10) :,} : GB {int(self.volume / 1024)}"