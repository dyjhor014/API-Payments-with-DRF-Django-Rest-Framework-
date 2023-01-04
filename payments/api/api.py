from datetime import datetime, timedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, filters
from payments.models import Services, Payment_user, Expired_payments
from payments.api.serializers import  ServiceSerializer, PaymentUserSerializer, ExpiredPaymentSerializer

class ServiceViewSet(viewsets.GenericViewSet):
    serializer_class = ServiceSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
    
    def list(self, request):
        """ 
        Lista todos los servicios

        name --> Nombre del servicio
        description --> Descripción del servicio
        logo --> Logotipo del servicio
        """
        service_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(service_serializer.data, status=status.HTTP_200_OK)

class PaymentUserViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentUserSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
    
    def list(self, request):
        payment_user = self.get_serializer(self.get_queryset(), many = True)
        return Response(payment_user.data, status=status.HTTP_200_OK)

    def create(self, request):
        payment_user = self.serializer_class(data=request.data)
        if payment_user.is_valid():
            payment_user.save()
            payment_date = datetime.strptime(payment_user.data["payment_date"], '%Y-%m-%d').date()
            expiration_date = datetime.strptime(payment_user.data["expiration_date"], '%Y-%m-%d').date()
            res = int(payment_date-expiration_date) / timedelta(days=1)
            if res > 0:
                print("Pago expirado")
            return Response({'message': 'Pago creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(payment_user.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk = None):
        if self.get_queryset(pk):
            payment_user = self.serializer_class(self.get_queryset(pk), data=request.data)
            if payment_user.is_valid():
                payment_user.save()
                return Response({'message': 'Pago actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response(payment_user.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        payment_user = self.get_queryset().filter(id=pk).first()
        if payment_user:
            payment_user.state = False
            payment_user.save()
            return Response({'message': 'Pago eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'message':'No existe un pago con esos datos'}, status=status.HTTP_400_BAD_REQUEST)
        
class ExpiredPaymentViewSet(viewsets.ModelViewSet):
    serializer_class = ExpiredPaymentSerializer

    def get_queryset(self):
        queryset = Expired_payments.objects.all()
        return queryset
