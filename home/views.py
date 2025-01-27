from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display_home(request):
    return render(request, 'home.html')

def display_processed(request):
    return render(request, 'processed.html')
