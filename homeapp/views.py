from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from .models import ForumPost, Mentorship
from .forms import ForumPostForm, MentorSearchForm, ContactMentorForm, MentorshipForm
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    return render(request, 'homeapp/index.html')

def dashboard(request):
    return render(request, 'homeapp/dashboard.html')

def about(request):
    return render(request, 'homeapp/about.html')

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
    """
    Handles mentor search, contact functionality, and displays mentorships.
    """
    search_results = None
    contact_form = None

    # Handle mentor search
    if request.method == 'POST' and 'search_mentor' in request.POST:
        search_form = MentorSearchForm(request.POST)
        if search_form.is_valid():
            preferred_language = search_form.cleaned_data['preferred_language']
            search_results = Mentorship.objects.filter(
                Q(preferred_language=preferred_language) & Q(mentor__isnull=False)
            )
    # Handle contact functionality
    elif request.method == 'POST' and 'contact_mentor' in request.POST:
        contact_form = ContactMentorForm(request.POST)
        if contact_form.is_valid():
            # Handle sending the message (e.g., save to database or send email)
            message = contact_form.cleaned_data['message']
            # Example: Save the message to the database (you'll need a Message model)
            # Message.objects.create(sender=request.user, recipient=mentor, content=message)
            return redirect('connect')
    else:
        search_form = MentorSearchForm()
        contact_form = ContactMentorForm()

    mentorships = Mentorship.objects.all()
    return render(request, 'homeapp/connections.html', {
        'mentorships': mentorships,
        'search_form': search_form,
        'search_results': search_results,
        'contact_form': contact_form
    })

@staff_member_required
def match_mentor(request):
    """
    Allows admins to match mentors to mentees.
    """
    if request.method == 'POST':
        form = MentorshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('match_mentor')
    else:
        form = MentorshipForm()

    mentorships = Mentorship.objects.all()
    return render(request, 'homeapp/match_mentor.html', {'form': form, 'mentorships': mentorships})

def post_detail(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    return render(request, 'homeapp/post_detail.html', {'post': post})