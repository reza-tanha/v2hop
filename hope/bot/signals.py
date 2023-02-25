from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth import get_user_model
from hope.account.models import Balance
User = get_user_model()


@receiver(post_save, sender=User)
def create_user_balance(sender, instance, created, **kwargs):
    if created:
        user_balance = Balance(
            user=instance, 
            balance=0
        )
        user_balance.save()