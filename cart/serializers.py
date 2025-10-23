from rest_framework import serializers
from .models import Cart
from products.serializers import ProdcutSerializer

class CartSerializer(serializers.ModelSerializer):
    product = ProdcutSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity', 'get_total_price']