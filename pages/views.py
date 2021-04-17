from django.shortcuts import render


# Home page view
def home(request):
    return render(request, 'pages/home.html')

# About page view
def about(request):
    return render(request, 'pages/about.html')

# Services page view
def services(request):
    return render(request, 'pages/services.html')

# Contact page view
def contact(request):
    return render(request, 'pages/contact.html')