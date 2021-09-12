from django.contrib import admin
from .models import Order, OrderItem, Product
admin.site.register(OrderItem)

import datetime
from django.http import HttpResponse

from django.urls import reverse
from django.utils.html import format_html

  

class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'last_name', 'email',
        'address', 'postal_code', 'city',
        'transport', 'created', 'status', 
    ]
    list_filter = ['created', 'updated']
