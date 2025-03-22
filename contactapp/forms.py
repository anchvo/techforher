from django import forms
from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "windows95-field"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class": "windows95-field"}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "windows95-field"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "windows95-field"}))
