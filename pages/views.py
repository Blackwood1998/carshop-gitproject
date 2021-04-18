from django.shortcuts import render
from .models import Team
from cars.models import Car


# Home page view
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by(
        '-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'pages/home.html', data)

# About page view


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

# Services page view


def services(request):
    return render(request, 'pages/services.html')

# Contact page view


def contact(request):
    return render(request, 'pages/contact.html')
