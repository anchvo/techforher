from . import views
from django.urls import path

urlpatterns = [
        path('', views.index, name='home'),
        path('about/', views.about, name='about'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('forum/', views.forum, name='forum'),
        path('connections/', views.connect, name='connections'),
        path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]