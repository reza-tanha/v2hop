# Generated by Django 3.2.9 on 2023-02-18 14:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ray', '0002_ordere'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ordere',
            new_name='Order',
        ),
    ]
