from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel
from users.models import User

# Create your models here.
#Modelo de la v1
class Payment(BaseModel):
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

    class Meta:
        db_table = 'payments'

#Modelos de la v2
class Services(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.URLField(max_length=5000)

    class Meta:
        db_table = 'services'

    def __str__(self):
        return self.name


class Payment_user(BaseModel):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(
        Services, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateField(null=True)
    expiration_date = models.DateField(null=True)
    payment_state = models.BooleanField('Estado_pago', default=False)
    penalty = models.FloatField(null=True)

    class Meta:
        db_table = 'payment_user'

    def __str__(self):
        return self.user_id


class Expired_payments(BaseModel):
    payment_user_id = models.ForeignKey(
        Payment_user, on_delete=models.CASCADE)
    penalty_fee_amount = models.FloatField()

    class Meta:
        db_table = 'expired_payments'

    def __str__(self):
        return self.payment_user_id