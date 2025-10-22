from rest_framework.viewsets import ModelViewSet
from .serializers import CartSerializer
from .models import Cart


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer