from django.urls import path
from .views import  MerchantViewSet
from rest_framework.routers import DefaultRouter

app_name = "classview"
urlpatterns = [

]

router = DefaultRouter()
router.register('shangjia', MerchantViewSet, basename='shangjia')
urlpatterns += router.urls