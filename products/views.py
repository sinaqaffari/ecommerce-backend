from rest_framework import viewsets
from .models import Product
from .serializers import ProdcutSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer