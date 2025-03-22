from . import views
from django.urls import path

app_name = 'contactapp-urls' # Defines the namespace

urlpatterns = [
        path('contact/', views.contact, name='contact'),
        path('success/', views.success, name='success'),
]