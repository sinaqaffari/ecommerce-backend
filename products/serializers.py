from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
          model = Category
          fields = ['id', 'name']        


class ProdcutSerializer(serializers.ModelSerializer):
        category = CategorySerializer()
        class Meta:
              model = Product
              fields= ['id', 'name', 'description', 'price', 'stock', 'category', 'image', 'created_at']