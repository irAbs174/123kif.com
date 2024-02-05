from django.urls import (path, include)
from .views import (index, insert_products)

urlpatterns = [
    path('', index),
    path('unique', insert_products),
]
