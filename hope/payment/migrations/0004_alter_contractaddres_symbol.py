# Generated by Django 4.0.1 on 2023-03-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_contractaddres_userpayments_wallat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractaddres',
            name='symbol',
            field=models.CharField(max_length=15, verbose_name='Symbol : USDT, TRX, '),
        ),
    ]
