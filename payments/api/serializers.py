from rest_framework import serializers
from payments.models import Payment, Services, Payment_user, Expired_payments

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'name', 'description', 'logo']

class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = ['id', 'user_id', 'service_id', 'amount', 'payment_date', 'expiration_date']

class ExpiredPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = ['id', 'payment_user_id', 'penalty_fee_amount']