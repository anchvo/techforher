from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from .models import ForumPost, Mentorship, Profile, CustomUser
from .forms import ForumPostForm, MentorSearchForm, ContactMentorForm, MentorshipForm

User = get_user_model()


def index(request):
    """Render the homepage."""
    return render(request, 'homeapp/index.html')


@login_required
def dashboard(request):
    """Render the user dashboard with posts and messages."""
    # Fetching the profile associated with the user
    profile = Profile.objects.filter(user=request.user).first()

    # Fetch recent posts from the forum
    posts = ForumPost.objects.all()[:5]
    messages = []  # Add your logic to fetch user-specific messages if applicable

    # Ensure request.user is a CustomUser instance
    if isinstance(request.user, CustomUser):
        user_instance = request.user
    else:
        user_instance = None  # Or redirect if necessary or raise an exception
        print("request.user is not a CustomUser instance")

    context = {
        'profile': profile,
        'user': user_instance,
        'posts': posts,
        'messages': messages
    }
    return render(request, 'homeapp/dashboard.html', context)


def about(request):
    """Render the About page."""
    return render(request, 'homeapp/about.html')


@login_required
def forum(request):
    """Handle forum post submissions and display forum posts."""
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            forum_post = form.save(commit=False)
            forum_post.user = request.user
            forum_post.save()
            return redirect('forum')
    else:
        form = ForumPostForm()

    posts = ForumPost.objects.all()
    return render(request, 'homeapp/forum.html', {'posts': posts, 'form': form})


@login_required
def connect(request):
    """Handles mentor search, contact functionality, and displays mentorships."""
    search_results = None
    contact_form = ContactMentorForm()
    search_form = MentorSearchForm()
    message_sent = False

    if request.method == 'POST' and 'search_mentor' in request.POST:
        search_form = MentorSearchForm(request.POST)
        if search_form.is_valid():
            preferred_language = search_form.cleaned_data['preferred_language']
            search_results = CustomUser.objects.filter(
                role='mentor',
                preferred_languages__name=preferred_language
            ).distinct()

    elif request.method == 'POST' and 'contact_mentor' in request.POST:
        contact_form = ContactMentorForm(request.POST)
        if contact_form.is_valid():
            mentor_id = request.POST.get('mentor_id')
            message = contact_form.cleaned_data['message']

            if mentor_id:
                mentor = get_object_or_404(CustomUser, id=mentor_id)
                print(f"Message sent to mentor: {mentor.username}")
                message_sent = True
        else:
            print("Contact form errors:", contact_form.errors)

    mentorships = Mentorship.objects.all()
    return render(request, 'homeapp/connections.html', {
        'mentorships': mentorships,
        'search_form': search_form,
        'search_results': search_results,
        'contact_form': contact_form,
        'message_sent': message_sent,
    })


@staff_member_required
def match_mentor(request):
    """Allows admins to match mentors to mentees."""
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
    """Display the details of a specific forum post."""
    post = get_object_or_404(ForumPost, id=post_id)
    return render(request, 'homeapp/post_detail.html', {'post': post})
