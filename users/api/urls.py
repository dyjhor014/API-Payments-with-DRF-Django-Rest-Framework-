from django.urls import path
from users.api.api import UserAPIView

urlpatterns = [
    path('usuario/', UserAPIView.as_view(), name= 'usuario_api'),
]
