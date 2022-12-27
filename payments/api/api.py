from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, filters
from payments.models import Services, Payment_user, Expired_payments
from payments.api.serializers import  ServiceSerializer, PaymentUserSerializer, ExpiredPaymentSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
    
    def list(self, request):
        print("Hola desde list")
        service_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(service_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        print("hola desde create")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Servicio creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk = None):
        print("Hola desde update")
        if self.get_queryset(pk):
            service_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if service_serializer.is_valid():
                service_serializer.save()
                return Response({'message': 'Servicio actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        print("Hola desde destroy")
        service = self.get_queryset().filter(id=pk).first()
        if service:
            service.state = False
            service.save()
            return Response({'message': 'Servicio eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'message':'No existe un servicio con esos datos'}, status=status.HTTP_400_BAD_REQUEST)

class PaymentUserViewSet(viewsets.ModelViewSet):
    queryset = Payment_user.objects.get_queryset().order_by('id')
    serializer_class = PaymentUserSerializer

class ExpiredPaymentViewSet(viewsets.ModelViewSet):
    queryset = Expired_payments.objects.get_queryset().order_by('id')
    serializer_class = ExpiredPaymentSerializer
