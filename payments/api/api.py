from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from payments.models import Payment
from payments.api.serializers import PaymentSerializer

@api_view(['GET','POST'])
def payment_api_view(request):
    #List
    if request.method == 'GET':
        #Query
        payments = Payment.objects.all()
        payments_serializer = PaymentSerializer(payments, many = True)
        return Response(payments_serializer.data, status=status.HTTP_200_OK)
    #Create
    elif request.method == 'POST':
        user_serializer = PaymentSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Pago creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors)
