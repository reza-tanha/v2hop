# Generated by Django 3.2.9 on 2023-02-20 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_perfectmonypayment_is_tmp'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingletonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PriceSettings',
            fields=[
                ('singletonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payment.singletonmodel')),
                ('price', models.FloatField(verbose_name='Price')),
                ('usd', models.IntegerField(verbose_name='usd')),
            ],
            bases=('payment.singletonmodel',),
        ),
    ]
