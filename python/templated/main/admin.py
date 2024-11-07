from django.contrib import admin
from .models import Contact, Order
# Register your models here.

admin.site.register(Order)
admin.site.register(Contact)