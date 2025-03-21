from . import views
from django.urls import path
from .views import (
    UserListView,
    UserDetailView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    MentorshipListView, 
    MentorshipDetailView, 
    MentorshipCreateView, 
    MentorshipUpdateView, 
    MentorshipDeleteView
)

urlpatterns = [
    path('', views.index, name='home'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('mentorships/', MentorshipListView.as_view(), name='mentorship-list'),
    path('mentorships/<int:pk>/', MentorshipDetailView.as_view(), name='mentorship-detail'),
    path('mentorships/create/', MentorshipCreateView.as_view(), name='mentorship-create'),
    path('mentorships/<int:pk>/update/', MentorshipUpdateView.as_view(), name='mentorship-update'),
    path('mentorships/<int:pk>/delete/', MentorshipDeleteView.as_view(), name='mentorship-delete'),
]

