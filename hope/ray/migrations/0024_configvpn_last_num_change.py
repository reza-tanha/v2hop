# Generated by Django 4.1.7 on 2023-02-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ray', '0023_rename_expier_date_configvpn_expire_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='configvpn',
            name='last_num_change',
            field=models.IntegerField(default=0, verbose_name='Last Change Server'),
        ),
    ]
