from django.contrib import admin

@admin.register(Event)
class AdminZone(admin.ModelAdmin):
    list_display = ('date', 'name', 'location', 'soil', 'moisture',
    	            'rainfall')
    list_filter = ('name', 'location')