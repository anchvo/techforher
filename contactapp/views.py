from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import generic

# Create your views here.

def contact(request):
    return render(request, 'contactapp/contact.html')

