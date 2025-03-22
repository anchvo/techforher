from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# ------------------------------------------
# CUSTOM USER MODEL
# ------------------------------------------
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('mentor', 'Mentor'),
        ('mentee', 'Mentee'),
    ]
    LANGUAGE_CHOICES = [
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('Java', 'Java'),
        ('CSS', 'CSS'),
        ('HTML', 'HTML'),
        ('PHP', 'PHP'),
        ('C#', 'C#'),
        ('Other', 'Other'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='mentee')
    preferred_languages = models.ManyToManyField('Language', blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name="customuser_groups",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name="customuser_permissions",
        related_query_name="customuser",
    )

    def __str__(self):
        return self.username

# ------------------------------------------
# LANGUAGE MODEL
# ------------------------------------------
class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# ------------------------------------------
# MENTORSHIP MODEL
# ------------------------------------------
class Mentorship(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]
    LANGUAGE_CHOICES = [
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('Java', 'Java'),
        ('CSS', 'CSS'),
        ('HTML', 'HTML'),
        ('PHP', 'PHP'),
        ('C#', 'C#'),
        ('Other', 'Other'),
    ]
    mentor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='mentorships_as_mentor')
    mentee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='mentorships_as_mentee')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    preferred_language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # NEW FIELD

    def __str__(self):
        return f"Mentorship: {self.mentor} → {self.mentee}"

# ------------------------------------------
# FORUM POST MODEL
# ------------------------------------------
class ForumPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="forum_posts")
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ------------------------------------------
# REPLY MODEL
# ------------------------------------------
class Reply(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="replies")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Reply by {self.user} on {self.post}"

# ------------------------------------------
# MESSAGE MODEL
# ------------------------------------------
class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # NEW FIELD to track unread messages

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"

# ------------------------------------------
# CONTACT REQUEST MODEL
# ------------------------------------------
class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

# ------------------------------------------
# USER PROFILE MODEL
# ------------------------------------------
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True, help_text="Store social media links")  # NEW FIELD

    def __str__(self):
        return f'{self.user.username} Profile'
