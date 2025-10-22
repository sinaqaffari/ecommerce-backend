from django.db import models
from orders.models import Order



class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)