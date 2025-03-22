from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import ContactForm

# Create your views here.

def contact(request):
    return render(request, 'contactapp/contact.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']


            # Combine user name with the subject
            full_subject = f"Contact Form: {name} - {subject}"

            # Send the email using Django's email_message function
            email_message = EmailMessage(
                full_subject,  # Combined subject (name + user-provided subject)
                message,  # The user message
                email,  # The user email
                [settings.EMAIL_HOST_USER],  # To email (email configured in settings.py)
                reply_to=[email],  # Ensure replies go to the user email
            )

            # Send the email using Django's EmailMessage
            email_message.send(fail_silently=False)  # If sending fails, an error will be raised

            # Redirect to the success page after the email is sent
            return redirect('contactapp-urls:success')
    else:
        form = ContactForm()
    return render(request, 'contactapp/contact.html', {'form': form})


def success(request):
    return render(request, 'contactapp/success.html')
