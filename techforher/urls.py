"""
URL configuration for techforher project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import SignupView
from homeapp.forms import CustomSignupForm
from django.shortcuts import render
from django.conf.urls import handler404, handler500
from .views import custom_404, custom_500
from django.views.defaults import page_not_found

urlpatterns = [
    path("", include("homeapp.urls"), name="homeapp-urls"),
    path("account/", include("allauth.urls")),
    path('account/signup/', SignupView.as_view(form_class=CustomSignupForm), name='account_signup'),
    path('admin/', admin.site.urls),
    path("contactapp/", include("contactapp.urls"), name="contactapp-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('404/', page_not_found, {'exception': Exception()}),
]

handler404 = custom_404
handler500 = custom_500
