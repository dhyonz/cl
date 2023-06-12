from django.contrib import admin
from .models import *

# Register your models here.

class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_Name', 'unit_Desc')
    list_display_links = ('unit_Name',)

admin.site.register(Unit, UnitAdmin)