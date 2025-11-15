from django.contrib import admin
from .models import *

admin.site.register(FarmerProfile)
# Land will be registered below with a custom ModelAdmin
@admin.register(AgriculturalEngineer)
class AgriculturalEngineerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'specialization',
        'experience_years',
        'contact',
    )

    list_filter = (
        'specialization',
    )

    search_fields = (
        'name',
        'specialization',
        'contact',
    )

    fieldsets = (
        ('Basic', {'fields': ('name', 'specialization')}),
        ('Details', {'fields': ('experience_years', 'contact', 'image')}),
    )


@admin.register(Veterinarian)
class VeterinarianAdmin(AgriculturalEngineerAdmin):
    """Admin view for the proxy Veterinarian model. Inherits display from AgriculturalEngineerAdmin."""
    pass
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'rental_price', 'available', 'website')
    list_filter = ('available',)
    search_fields = ('name', 'description', 'owner__username')
    fieldsets = (
        (None, {'fields': ('owner', 'name', 'description')}),
        ('Pricing & Availability', {'fields': ('rental_price', 'available', 'website')}),
        ('Media', {'fields': ('image',)}),
    )

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('type', 'breed', 'price')

@admin.register(AnimalFeed)
class AnimalFeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name', 'description')
    fieldsets = (
        (None, {'fields': ('seller', 'name', 'description')}),
        ('Website & Media', {'fields': ('website', 'image')}),
    )

@admin.register(Aggregator)
class AggregatorAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact', 'website')
    search_fields = ('company_name', 'service_description')
    fieldsets = (
        (None, {'fields': ('company_name', 'service_description')}),
        ('Contact', {'fields': ('contact', 'website')}),
        ('Media', {'fields': ('image',)}),
    )

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