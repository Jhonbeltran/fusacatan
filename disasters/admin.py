from django.contrib import admin
from .models import Disaster

@admin.register(Disaster)
class AdminDisaster(admin.ModelAdmin):
    list_display = ('date', 'name', 'location', 'deceases',
    	            'material_losses')
    list_filter = ('date', 'name', 'location')
