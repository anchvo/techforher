from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import ForumPost
# Create your views here.


def index(request):
    return render(request, 'homeapp/index.html')

def dashboard(request):
    return render(request, 'homeapp/dashboard.html')

def about(request):
    return render(request, 'homeapp/about.html')

def forum(request):
    posts = ForumPost.objects.all()
    return render(request, 'homeapp/forum.html', {'posts': posts})

def connect(request):
    return render(request, 'homeapp/connections.html')

def post_detail(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    return render(request, 'homeapp/post_detail.html', {'post': post})