from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.


def index(request):
    return render(request, 'homeapp/index.html')

def dashboard(request):
    return render(request, 'homeapp/dashboard.html')

def about(request):
    return render(request, 'homeapp/about.html')

def forum(request):
    return render(request, 'homeapp/forum.html')

def connect(request):
    return render(request, 'homeapp/connections.html')