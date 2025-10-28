"""
URL configuration for django_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import CustomTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/orders/', include('orders.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/products/', include('products.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name="token_obtain"), #JWT endpoints
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"), #JWT endpoints
    path('api/users/<int:pk>/', UserDetailView.as_view(), name="user_detail_view"),
]
