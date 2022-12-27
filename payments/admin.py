from django.contrib import admin
from payments.models import Services, Payment_user, Expired_payments

# Register your models here.
admin.site.register(Services)
admin.site.register(Payment_user)