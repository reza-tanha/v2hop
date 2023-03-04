# Generated by Django 4.1.7 on 2023-03-03 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ray", "0002_config_delete_configvpn"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProxyConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("conf", models.TextField(unique=True, verbose_name="HashV2ray")),
                ("uuid", models.TextField(blank=True, null=True, verbose_name="uuid")),
                (
                    "volume",
                    models.IntegerField(default=150, verbose_name="Volume : MB"),
                ),
                (
                    "last_num_change",
                    models.IntegerField(default=0, verbose_name="Last Change Server"),
                ),
                (
                    "is_use",
                    models.BooleanField(
                        default=False, verbose_name="Is this configuration used?"
                    ),
                ),
                (
                    "expire_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Expire Date Time"
                    ),
                ),
                (
                    "server",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="proxy_config",
                        to="ray.server",
                        verbose_name="server",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="proxy_config",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Config",
        ),
    ]
