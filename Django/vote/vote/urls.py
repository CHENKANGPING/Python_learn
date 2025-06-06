"""
URL configuration for vote project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from polls.views import show_subjects, show_teachers, praise_or_criticize, login, logout, get_captcha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_subjects),
    path('teachers/', show_teachers, name='teachers'),
    path('praise/', praise_or_criticize, name='praise'),
    path('criticize/', praise_or_criticize, name='criticize'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('captcha/', get_captcha, name='captcha'),
]