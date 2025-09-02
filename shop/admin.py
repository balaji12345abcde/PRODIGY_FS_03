from django.contrib import admin
from .models import Product, Review, Order, SupportQuery

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','created_at')
    search_fields = ('name','category')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name','product','rating','created_at')
    search_fields = ('user_name','product__name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','total','status','created_at')
    list_filter = ('status',)

@admin.register(SupportQuery)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('name','email','resolved','created_at')
    list_filter = ('resolved',)
