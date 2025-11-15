from django.db import models
from django.contrib.auth.models import User

# ---- Farmer Profile ----
class FarmerProfile(models.Model):
    EXPERIENCE_CHOICES = [
        ('new', 'New Farmer'),
        ('experienced', 'Experienced Farmer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

# ---- Land ----
class Land(models.Model):
    LAND_TYPE_CHOICES = [
        ('agricultural', 'Agricultural Land'),
        ('farm', 'Farm Land'),
        ('orchard', 'Orchard'),
        ('ranch', 'Ranch'),
        ('other', 'Other'),
    ]
    
    # Basic Information
    title = models.CharField(max_length=200)
    description = models.TextField()
    land_type = models.CharField(max_length=20, choices=LAND_TYPE_CHOICES, default='agricultural')
    location = models.CharField(max_length=100)
    
    # Specifications
    area = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total area in hectares")
    price = models.DecimalField(max_digits=12, decimal_places=2, help_text="Total price for the entire land")
    
    # Contact Information
    contact_name = models.CharField(max_length=100, default="Unknown Owner")
    contact_phone = models.CharField(max_length=20, default="0612345678")
    
    # Image
    image = models.ImageField(upload_to='lands/', blank=True, null=True)
    
    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.location}"

    @property
    def main_image(self):
        """Compatibility alias used in templates: return the primary image field."""
        return self.image

    @property
    def price_per_hectare(self):
        try:
            return float(self.price) / float(self.area) if self.area else 0
        except Exception:
            return 0

# Product model removed — products are no longer part of the application

# ---- Agricultural Engineer (Added by Admin Only) ----
class AgriculturalEngineer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    contact = models.CharField(max_length=50)
    image = models.ImageField(upload_to='engineers/', blank=True, null=True)

    def __str__(self):
        return self.name

# ---- Equipment for Rent ----
class Equipment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='equipment/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# ---- Animal Market ----
class Animal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField(help_text='Age in months', verbose_name='Age (months)')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='animals/', blank=True, null=True)

    def __str__(self):
        return f"{self.type} - {self.breed}"

# ---- Animal Feed ----
class AnimalFeed(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='feed/', blank=True, null=True)

    def __str__(self):
        return self.name

# ---- Aggregator ----
class Aggregator(models.Model):
    company_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    service_description = models.TextField()
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='aggregators/', blank=True, null=True)

    def __str__(self):
        return self.company_name


# Proxy model to expose a separate admin section named "Veterinarian"
class Veterinarian(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    contact = models.CharField(max_length=50)
    image = models.ImageField(upload_to='veterinarians/', blank=True, null=True)

    class Meta:
        verbose_name = 'Veterinarian'
        verbose_name_plural = 'Veterinarians'

    def __str__(self):
        return self.name