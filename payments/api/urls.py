from django.urls import path
from payments.api.api import payment_api_view

urlpatterns = [
    path('payments/', payment_api_view, name= 'payments'),
]