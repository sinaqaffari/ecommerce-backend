from rest_framework import generics
from .models import CustomUser 
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework_simplejwt.settings import api_settings as SIMPLE_JWT


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class =  UserSerializer
    permission_classes = [IsAuthenticated]


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request ,*args, **kwargs)
        response.data['expires_in'] = SIMPLE_JWT.ACCESS_TOKEN_LIFETIME.total_seconds()
        return response