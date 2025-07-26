from django.urls import path

from .views import merchant,category

app_name = 'serialize'

urlpatterns = [
    path('merchant/', merchant, name='merchant'),
    path('category/',category,name='category'),
]