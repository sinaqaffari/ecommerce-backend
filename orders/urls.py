from rest_framework.routers import DefaultRouter
from .views import OrdersViewSet


router = DefaultRouter()
router.register(r'', OrdersViewSet)

urlpatterns = router.urls