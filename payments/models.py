from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel
from users.models import User

# Create your models here.
class Payments(BaseModel):
    class Services(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users')
    service = models.CharField(
        max_length=2,
        choices=Services.choices,
        default=Services.NETFLIX,
    )
    amount = models.FloatField(default=0.0)
    payment_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(auto_now=False, auto_now_add=True, blank=True)

    class Meta:
        db_table = 'payments'
