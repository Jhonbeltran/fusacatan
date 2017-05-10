from django.contrib import admin
from .models import Zone

@admin.register(Zone)
class AdminZone(admin.ModelAdmin):
    list_display = ('date', 'name', 'location', 'soil', 'moisture',
    	            'rainfall')
    list_filter = ('name', 'location')