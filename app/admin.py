from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Consigner, Consignee, Vehicle, Invoice

@admin.register(Consigner)
class ConsignerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gst_no', 'state_code', 'address')
    search_fields = ('name', 'gst_no', 'state_code')

@admin.register(Consignee)
class ConsigneeAdmin(admin.ModelAdmin):
    list_display = ('name', 'gst_no', 'state_code', 'address')
    search_fields = ('name', 'gst_no', 'state_code')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('truck_no', 'driver_name', 'contact_no', 'owner_name')
    search_fields = ('truck_no', 'driver_name', 'owner_name')

    fieldsets = (
        ('Vehicle Information', {
            'fields': ('truck_no', 'driver_name', 'driver_address', 'contact_no', 'engine_no', 'chasis_no', 'dl_no')
        }),
        ('Owner Information', {
            'fields': ('owner_name', 'owner_address', 'owner_contact', 'owner_pan')
        }),
    )
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'from_field', 'to_field', 'consigner', 'consignee', 'nature_of_goods', 'weight', 'freight_total', 'payable_amt', 'date')
    search_fields = ('invoice_number', 'from_field', 'to_field', 'consigner__name', 'consignee__name', 'nature_of_goods')

    fieldsets = (
        ('Invoice Information', {
            'fields': ('invoice_number', 'date')
        }),
        ('Location Information', {
            'fields': ('from_field', 'to_field')
        }),
        ('Consigner and Consignee', {
            'fields': ('consigner', 'consignee')
        }),
        ('Goods Information', {
            'fields': ('nature_of_goods', 'weight')
        }),
        ('Freight Details', {
            'fields': ('freight_rate', 'freight_total', 'toll_tax', 'gr_sr_charges')
        }),
        ('Expenses', {
            'fields': ('fooding', 'kata', 'gst', 'advance', 'payable_amt')
        }),
        ('E-Way Bill', {
            'fields': ('e_way_bill_no',)
        }),
    )

    readonly_fields = ('invoice_number', 'payable_amt')  # Make invoice_number and payable_amt read-only in the admin interface

    def save_model(self, request, obj, form, change):
        # Calculate payable_amt based on other fields if needed before saving
        obj.payable_amt = obj.freight_total + obj.toll_tax + obj.gr_sr_charges + obj.fooding - obj.advance
        super().save_model(request, obj, form, change)