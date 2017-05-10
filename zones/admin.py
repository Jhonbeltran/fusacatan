from django.contrib import admin
from .models import Zone

@admin.register(Zone)
class AdminZone(admin.ModelAdmin):
    list_display = ('date', 'location', 'moisture',
    	            'rainfall', 'trees')
    list_filter = ('location', 'location')