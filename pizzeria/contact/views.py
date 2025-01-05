from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, 'contact/contact.html')

def home_service(request):
    return render(request, 'contact/home-service.html')
