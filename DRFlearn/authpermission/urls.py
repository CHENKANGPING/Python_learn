from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MerchantViewSet, token_view

router = DefaultRouter()
router.register('merchant', MerchantViewSet, basename='merchant')
urlpatterns = [
    path('token/',token_view,name='token'),
              ] + router.urls