from django import forms
from .models import ForumPost, Mentorship

class ForumPostForm(forms.ModelForm):
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
        widget=forms.Textarea(attrs={'rows': 4}),
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