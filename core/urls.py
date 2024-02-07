from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("unique/", admin.site.urls),
    path('', include('shop.router')),
]
