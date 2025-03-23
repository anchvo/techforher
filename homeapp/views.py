from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import ForumPost, Mentorship, Profile, CustomUser, Message, Reply
from .forms import ForumPostForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from .models import ForumPost, Mentorship, CustomUser
from .forms import ForumPostForm, MentorSearchForm, ContactMentorForm, MentorshipForm, UserForm
from django.contrib.auth import get_user_model
from .forms import ProfileForm, UserForm, ReplyForm

User = get_user_model()


def index(request):
    return render(request, 'homeapp/index.html')


@login_required
def dashboard(request):
    if request.user.is_authenticated and isinstance(request.user, CustomUser): #added CustomUser check
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = None  # Handle the case where no profile exists.

        posts = ForumPost.objects.all()[:5]  # Get the latest 5 posts
        messages = Message.objects.filter(receiver=request.user)  
        preferred_languages = request.user.preferred_languages.all()
        context = {'profile': profile, 'user': request.user, 'posts': posts, 'messages': messages, 'preferred_languages': preferred_languages}
    else:
        context = {'user': request.user}
    return render(request, 'homeapp/dashboard.html', context)

def about(request):
    return render(request, 'homeapp/about.html')


@login_required
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


@login_required
def connect(request):
    """
    Handles mentor search, contact functionality, and displays mentorships.
    """
    search_results = None
    contact_form = ContactMentorForm()  # Initialize contact_form
    search_form = MentorSearchForm()  # Initialize search_form
    match_form = MentorshipForm()  # Initialize match_form
    message_sent = False

    # Handle mentor search
    if request.method == 'POST' and 'search_mentor' in request.POST:
        search_form = MentorSearchForm(request.POST)
        if search_form.is_valid():
            preferred_language = search_form.cleaned_data['preferred_language']
            # Filter mentors based on role and preferred languages
            search_results = CustomUser.objects.filter(
                role='mentor',
                preferred_languages__name=preferred_language
            ).distinct()

    # Handle contact functionality
    elif request.method == 'POST' and 'contact_mentor' in request.POST:
        contact_form = ContactMentorForm(request.POST)
        if contact_form.is_valid():
            mentor_id = request.POST.get('mentor_id')
            message = contact_form.cleaned_data['message']
            if mentor_id:
                mentor = CustomUser.objects.get(id=mentor_id)
                Message.objects.create(sender=request.user, receiver=mentor, content=message)
                print(f"Message sent to mentor: {mentor.username}")
                message_sent = True


    mentorships = Mentorship.objects.all()
    return render(request, 'homeapp/connections.html', {
        'mentorships': mentorships,
        'search_form': search_form,
        'search_results': search_results,
        'contact_form': contact_form,
        'match_form': match_form,
        'message_sent': message_sent
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


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    replies = post.replies.all()
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.user = request.user
            reply.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = ReplyForm()
    return render(request, 'homeapp/post_detail.html', {'post': post, 'replies': replies, 'form': form})


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    user_form = UserForm(instance=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('dashboard')  # Adjust as needed
    else:
        profile_form = ProfileForm(instance=profile)

    return render(request, 'homeapp/profile.html', {'form': profile_form, 'user_form': user_form})