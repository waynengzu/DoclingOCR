from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display_index(request):
    return render(request, 'index.html')

def display_process(request):
    return render(request, 'process.html')

def display_analyze(request):
    return render(request, 'analyze.html')


