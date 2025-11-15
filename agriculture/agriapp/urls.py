from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('land/', views.land_view, name='land'),
    path('animals/', views.animals_view, name='animals'),
    path('engineers/', views.engineers_view, name='engineers'),
    # products removed
    path('equipments/', views.equipments_view, name='equipments'),
    path('animal_feeds/', views.animal_feeds_view, name='animal_feeds'),
    path('aggregators/', views.aggregators_view, name='aggregators'),
    path('veterinarian/', views.veterinarian_view, name='veterinarian'),
    
    # Add routes for model creation (admin only)
    path('land/add/', views.land_add_view, name='land_add'),
    path('engineers/add/', views.engineer_add_view, name='engineer_add'),
    path('equipments/add/', views.equipment_add_view, name='equipment_add'),
    path('animals/add/', views.animal_add_view, name='animal_add'),
    path('animal_feeds/add/', views.feed_add_view, name='feed_add'),
    path('aggregators/add/', views.aggregator_add_view, name='aggregator_add'),
]