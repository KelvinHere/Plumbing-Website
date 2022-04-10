from django.contrib import admin
from .models import Product, Brand, Shop, Category

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', ]

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shop)