from django import forms
from .models import (
	Land, Equipment, Animal, AnimalFeed,
	AgriculturalEngineer, Aggregator
)


class LandForm(forms.ModelForm):
	class Meta:
		model = Land
		fields = [
			'title', 'description', 'land_type', 'location',
			'area', 'price', 'contact_name', 'contact_phone', 'image'
		]


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'description', 'rental_price', 'image', 'available']
class AnimalForm(forms.ModelForm):
	class Meta:
		model = Animal
		fields = ['type', 'breed', 'age', 'price', 'location', 'image']
		labels = {
			'age': 'Age (months)'
		}
class AnimalFeedForm(forms.ModelForm):
    class Meta:
        model = AnimalFeed
        fields = ['name', 'description', 'website', 'image']
class AgriculturalEngineerForm(forms.ModelForm):
	class Meta:
		model = AgriculturalEngineer
		fields = ['name', 'specialization', 'experience_years', 'contact', 'image']


class AggregatorForm(forms.ModelForm):
	class Meta:
		model = Aggregator
		fields = ['company_name', 'contact', 'service_description', 'image']


