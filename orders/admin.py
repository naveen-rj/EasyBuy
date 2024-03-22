from typing import Any
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import Order, OrderItem

# Register your models here.

class OrderAdmin(ModelAdmin):
    list_display = ('id', 'owner', 'total_amount', 'order_status', 'created_at')
    list_filter = ('owner', 'created_at', 'order_status')
    search_fields = ('id', 'owner__name')
    list_editable = ('total_amount',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    def save_model(self, request, obj, form, change):
        # Check if the order status has been changed
        if 'order_status' in form.changed_data:
            # Call the set_status method to update the order status and timestamp
            obj.set_status(form.cleaned_data['order_status'])
        # Save the object
        obj.save()
        
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)