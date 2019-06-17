from django.contrib import admin
from .models import Order, OrderItem, CartItem

admin.site.register([Order, OrderItem, CartItem])
# Register your models here.
