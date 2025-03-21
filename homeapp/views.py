from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import User
from .models import Mentorship


# Create your views here.


def index(request):
    return render(request, 'homeapp/index.html')

# List all users
class UserListView(ListView):
    model = User
    template_name = 'homeapp/user_list.html'
    context_object_name = 'users'

# Display user details
class UserDetailView(DetailView):
    model = User
    template_name = 'homeapp/user_detail.html'
    context_object_name = 'user'

# Create a new user
class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'role', 'is_verified']
    template_name = 'homeapp/user_form.html'
    success_url = reverse_lazy('user-list')

# Update an existing user
class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'role', 'is_verified']
    template_name = 'homeapp/user_form.html'
    success_url = reverse_lazy('user-list')

# Delete a user
class UserDeleteView(DeleteView):
    model = User
    template_name = 'homeapp/user_confirm_delete.html'
    success_url = reverse_lazy('user-list')

# List all mentorships
class MentorshipListView(ListView):
    model = Mentorship
    template_name = 'mentorship/mentorship_list.html'
    context_object_name = 'mentorships'

# Display mentorship details
class MentorshipDetailView(DetailView):
    model = Mentorship
    template_name = 'mentorship/mentorship_detail.html'
    context_object_name = 'mentorship'

# Create a new mentorship (only logged-in users)
@method_decorator(login_required, name='dispatch')
class MentorshipCreateView(CreateView):
    model = Mentorship
    fields = ['mentor', 'mentee', 'status', 'preferred_language']
    template_name = 'mentorship/mentorship_form.html'
    success_url = reverse_lazy('mentorship-list')

# Update an existing mentorship (only logged-in users)
@method_decorator(login_required, name='dispatch')
class MentorshipUpdateView(UpdateView):
    model = Mentorship
    fields = ['status', 'preferred_language']
    template_name = 'mentorship/mentorship_form.html'
    success_url = reverse_lazy('mentorship-list')

# Delete a mentorship (only logged-in users)
@method_decorator(login_required, name='dispatch')
class MentorshipDeleteView(DeleteView):
    model = Mentorship
    template_name = 'mentorship/mentorship_confirm_delete.html'
    success_url = reverse_lazy('mentorship-list')