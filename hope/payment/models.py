from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class PerfectMonyPayment(models.Model):
    
    user = models.ForeignKey(
        to=User,
        related_name="user_pm_payment",
        verbose_name="User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    voucher_code = models.CharField(
        verbose_name="voucher_code",
        max_length=30,
        null=True,
        blank=True
    )
    
    voucher_active = models.CharField(
        verbose_name="voucher_active",
        max_length=30,
        null=True,
        blank=True
    )
    
    date = models.DateTimeField(
        auto_now_add=True
    )
    
    status = models.BooleanField(
        default=False,
        verbose_name="Status"
    )
    
    is_tmp = models.BooleanField(
        default=True,
        verbose_name="is_tmp"
    )
    
    def __str__(self) -> str:
        return f"{str(self.user.user_id)} : {self.user.first_name}" 
    
    

class SingletonModel(models.Model):
    def save(self, *args, **kwargs):
        self.id=1
        return super().save(*args, **kwargs)
    
class PriceSettings(SingletonModel):
    price = models.IntegerField(
        verbose_name="Price : Rial",
    )
    
    usd = models.FloatField(
        verbose_name="usd : Usd"
    )
    
    def __str__(self):
        return f"${self.price} : {self.usd}"