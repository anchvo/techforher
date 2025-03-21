from . import views
from django.urls import path

urlpatterns = [
        path('', views.index, name='home'),
        path('about/', views.about, name='about'),
        path('profile/', views.profile, name='profile'),
        path('forum/', views.forum, name='forum'),
        path('connect/', views.connect, name='connect'),
]