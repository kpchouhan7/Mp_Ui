from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('english/', views.english_view, name='english'),
    path('french/', views.french_view, name='french'),
    path('spanish/', views.spanish_view, name='spanish'),
]