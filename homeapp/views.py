from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import ForumPost, Mentorship
from .forms import ForumPostForm
from django.contrib.auth import get_user_model
# Create your views here.


def index(request):
    return render(request, 'homeapp/index.html')

def dashboard(request):
    return render(request, 'homeapp/dashboard.html')

def about(request):
    return render(request, 'homeapp/about.html')

User = get_user_model()

def forum(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            forum_post = form.save(commit=False)
            forum_post.user = User.objects.get(pk=request.user.pk)
            forum_post.save()
            return redirect('forum')
    else:
        form = ForumPostForm()
    posts = ForumPost.objects.all()
    return render(request, 'homeapp/forum.html', {'posts': posts, 'form': form})

def connect(request):
    mentorships = Mentorship.objects.all()  # Fetch all mentorships
    return render(request, 'homeapp/connections.html', {'mentorships': mentorships})

def post_detail(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    return render(request, 'homeapp/post_detail.html', {'post': post})