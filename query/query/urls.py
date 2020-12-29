"""query URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from annotate.views import Hello, Login, WriterViewSet, BookViewSet

router = routers.DefaultRouter()
router.register('writer', WriterViewSet, basename='writer')
router.register('book', BookViewSet, basename='book')


urlpatterns = [
    path('hello/', Hello.as_view(), name='hello'),
    path('login/', Login.as_view(), name='login'),
    path('', include(router.urls))
]