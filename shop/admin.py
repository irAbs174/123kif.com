from django.contrib import admin
from .models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_sku', 'product_regular_price', 'product_price', 'product_created_at', 'product_updated_at')
    list_filter = ('product_id', 'product_sku', 'product_regular_price', 'product_price')
    search_fields = ('product_created_at', 'product_updated_at')

admin.site.register(Products, ProductsAdmin)
