from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProdcutSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProdcutSerializer