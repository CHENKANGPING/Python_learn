from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'absent'

router = DefaultRouter(trailing_slash=False)
router.register(r'absent',views.AbsentViewSet, basename='absent')

urlpatterns = [] + router.urls