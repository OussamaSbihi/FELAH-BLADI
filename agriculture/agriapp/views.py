from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        experience = request.POST['experience']
        username = email
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')

        user = User.objects.create_user(
            username=username, 
            password=password,
            first_name=first_name, 
            last_name=last_name, 
            email=email
        )
        
        # Create Farmer Profile if the model exists
        try:
            from .models import FarmerProfile
            FarmerProfile.objects.create(
                user=user,
                phone=phone,
                experience=experience
            )
        except:
            pass  # Skip if FarmerProfile doesn't exist
        
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Land  # Add this import
def land_view(request):
    try:
        # Get all land listings
        lands = Land.objects.all().order_by('-created_at')
        
        context = {
            'lands': lands,
            'total_lands': lands.count(),
        }
    except Exception as e:
        # Fallback if there's any error
        context = {
            'lands': [],
            'total_lands': 0,
        }
    
    return render(request, 'land.html', context)

def animals_view(request):
    # Display animals from database
    try:
        from .models import Animal
        animals = Animal.objects.all().order_by('-id')
    except Exception:
        animals = []
    return render(request, 'animals.html', {'animals': animals})

def engineers_view(request):
    # Display all AgriculturalEngineers
    from .models import AgriculturalEngineer
    engineers = AgriculturalEngineer.objects.all()
    return render(request, 'engineers.html', {'engineers': engineers})

def products_view(request):
    # Products were removed from the application — redirect to home
    return redirect('home')

def equipments_view(request):
    # Display equipments from database
    try:
        equipments = Equipment.objects.filter(available=True).order_by('-id')
    except Exception:
        equipments = []
    return render(request, 'equipments.html', {'equipments': equipments})

def animal_feeds_view(request):
    # Display animal feeds from database
    try:
        feeds = AnimalFeed.objects.all().order_by('-id')
    except Exception:
        feeds = []
    return render(request, 'animal_feeds.html', {'feeds': feeds})

def aggregators_view(request):
    # Display aggregators from database
    try:
        aggs = Aggregator.objects.all().order_by('-id')
    except Exception:
        aggs = []
    return render(request, 'aggregators.html', {'aggregators': aggs})

def veterinarian_view(request):
    """Display list of AgriculturalEngineers as veterinarians."""
    from .models import Veterinarian
    engineers = Veterinarian.objects.all()
    return render(request, 'veterinarian.html', {'engineers': engineers})


# Admin-only add views for model creation
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from .forms import (
    LandForm, EquipmentForm, AnimalForm, 
    AnimalFeedForm, AgriculturalEngineerForm, AggregatorForm
)
from .models import AgriculturalEngineer, Equipment, Animal, AnimalFeed, Aggregator


@user_passes_test(lambda u: u.is_superuser)
def land_add_view(request):
    # Site add pages are disabled; use Django admin to add Land entries.
    return redirect('admin:index')


@user_passes_test(lambda u: u.is_superuser)
def engineer_add_view(request):
    # Site add pages are disabled; use Django admin to add AgriculturalEngineer entries.
    return redirect('admin:index')

@user_passes_test(lambda u: u.is_superuser)
def equipment_add_view(request):
    # Site add pages are disabled; use Django admin to add Equipment entries.
    return redirect('admin:index')


@user_passes_test(lambda u: u.is_superuser)
def animal_add_view(request):
    # Site add pages are disabled; use Django admin to add Animal entries.
    return redirect('admin:index')


@user_passes_test(lambda u: u.is_superuser)
def feed_add_view(request):
    # Site add pages are disabled; use Django admin to add AnimalFeed entries.
    return redirect('admin:index')
def aggregator_add_view(request):
    # Site add pages are disabled; use Django admin to add Aggregator entries.
    return redirect('admin:index')