from django.contrib import admin
from .models import *

# Register your models here.

class PreventiveMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('wo_Number', 'pvm_Number', 'unit_Maintenance', 'insp_Date', 'pic')
    list_display_links = ('wo_Number',)

admin.site.register(PreventiveMaintenance, PreventiveMaintenanceAdmin)

# class UnitAdmin(admin.ModelAdmin):
#     list_display = ('unit_Name', 'unit_Desc')
#     list_display_links = ('unit_Name',)

# admin.site.register(Unit, UnitAdmin)