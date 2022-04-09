from django.contrib import admin

from api.models import Parameter

# Register your models here.

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ['created', 'voltage_r', 'current_r', 'voltage_y', 'current_y', 'voltage_b', 'current_b', 'power_r', 'power_y', 'power_b']
    list_filter = ['created']