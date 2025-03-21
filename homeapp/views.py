from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User


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
