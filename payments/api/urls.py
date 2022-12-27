from django.urls import path
from payments.api.api import payment_api_view, payment_user_api_view, expired_payment_api_view

urlpatterns = [
    path('payment/', payment_api_view, name= 'payments'),
    path('payment_user/', payment_user_api_view, name= 'payments_user'),
    path('payment_expired/', expired_payment_api_view, name='payments_expired')
]