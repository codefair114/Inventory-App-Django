from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
admin.site.site_header = 'Game Night Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category')
    list_filter = ['category']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Series)
admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(PaymentMethod)
admin.site.register(Contract)
admin.site.register(Shipment)
admin.site.register(OrderClient)