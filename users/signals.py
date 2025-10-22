from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.conf import settings
from django.contrib.auth import get_user_model
# from cart.models import Cart

User = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_cart_for_new_user(sender, instace, created, **kwargs):
    if created:
        # you can create an empty cart 
        print(f"Cart setup for : {instace.username}")