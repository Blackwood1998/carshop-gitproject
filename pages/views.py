from django.shortcuts import render
from .models import Team


# Home page view
def home(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
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