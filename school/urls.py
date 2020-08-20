"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import permissions

from core.authentication import MyTokenObtainPairSerializer, MyTokenObtainPairView
from core.views import login
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [path('admin/', admin.site.urls),
    #path('', include('students.urls')),
    #path('', include('teachers.urls')),
    path('', include('subjects.urls')),
    path('accounts/login/', login),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
