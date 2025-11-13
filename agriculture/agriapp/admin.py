from django.contrib import admin
from .models import *

admin.site.register(FarmerProfile)
# Land will be registered below with a custom ModelAdmin
admin.site.register(Product)
admin.site.register(AgriculturalEngineer)
admin.site.register(Equipment)
admin.site.register(Animal)
admin.site.register(AnimalFeed)
admin.site.register(Aggregator)

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'location',
        'area',
        'price',
        'created_at',
    ]

    list_filter = [
        'land_type',
        'created_at',
    ]

    search_fields = [
        'title',
        'description',
        'location',
        'contact_name',
    ]

    readonly_fields = ['created_at']

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'title',
                'description',
                'land_type',
                'location',
            )
        }),
        ('Specifications', {
            'fields': (
                'area',
                'price',
            )
        }),
        ('Contact Information', {
            'fields': (
                'contact_name',
                'contact_phone',
            )
        }),
        ('Image', {
            'fields': (
                'image',
            )
        }),
        ('Meta', {
            'fields': (
                'created_at',
            )
        }),
    )