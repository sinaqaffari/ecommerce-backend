from rest_framework import generics
from .models import CustomUser 
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class =  UserSerializer
    permission_classes = [IsAuthenticated]
