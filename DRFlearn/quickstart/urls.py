from rest_framework.routers import DefaultRouter

from quickstart.views import MerchantViewSet

router = DefaultRouter()
router.register('merchant', MerchantViewSet)

app_name = 'quickstart'
urlpatterns = [] + router.urls
