from rest_framework.routers import DefaultRouter
from .views import CartViewSet


router = DefaultRouter()
router.register(r'', CartViewSet)

urlpatterns = router.urls