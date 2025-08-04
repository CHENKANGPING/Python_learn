from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'absent'

router = DefaultRouter(trailing_slash=False)
router.register(r'absent', views.AbsentViewSet, basename='absent')

urlpatterns = [
                  path('type', views.AbsentTypeView.as_view(), name='absenttypes'),
                  path('responder', views.ResponderView.as_view(), name='getresponder'),
              ] + router.urls
