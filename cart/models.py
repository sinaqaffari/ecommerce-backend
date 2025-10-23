from django.db import models
from products.models import Product
from django.conf import settings



class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def get_total_price(self): 
        return self.product.price * self.quantity