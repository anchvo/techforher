from django import forms
from .models import ForumPost, Mentorship, CustomUser, Language
from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    '''
    Custom signup form to include role and preferred languages.
    '''
    role = forms.ChoiceField(
    choices=CustomUser.ROLE_CHOICES, 
    required=True, 
    label='Role')
    preferred_languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(), 
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Preferred Languages'
    )

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['role'].widget.attrs.update({'class': 'form-control'})
        self.fields['preferred_languages'].widget.attrs.update({'class': 'form-control'})

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.role = self.cleaned_data['role']
        user.preferred_languages.set(self.cleaned_data['preferred_languages'])
        user.save()
        return user


class ForumPostForm(forms.ModelForm):
    """
    Form for creating and editing forum posts.
    The user field is assigned automatically in the view.
    """
    class Meta:
        model = ForumPost
        fields = ['title', 'content', 'is_anonymous']

class MentorSearchForm(forms.Form):
    """
    Form to search for mentors based on preferred language.
    """
    preferred_language = forms.ChoiceField(
        choices=Mentorship.LANGUAGE_CHOICES,
        label="Preferred Language",
        required=True
    )

class ContactMentorForm(forms.Form):
    """
    Form to send a message to a mentor.
    """
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your message...'}),
        label="Message",
        required=True
    )

class MentorshipForm(forms.ModelForm):
    """
    Form for admins to match mentors and mentees.
    """
    class Meta:
        model = Mentorship
        fields = ['mentor', 'mentee', 'status', 'preferred_language']
