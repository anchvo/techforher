from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import User, Mentorship, ForumPost, Message, ContactRequest, Reply

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_verified', 'date_joined')
    list_filter = ('role', 'is_verified')
    search_fields = ('username', 'email')

@admin.register(Mentorship)
class MentorshipAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'status', 'preferred_language', 'created_at')
    list_filter = ('status', 'preferred_language')
    search_fields = ('mentor__username', 'mentee__username')

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_anonymous', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'is_anonymous')
    search_fields = ('title', 'user__username', 'content')

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'is_approved')
    search_fields = ('user__username', 'post__title', 'content')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'created_at')
    search_fields = ('sender__username', 'receiver__username', 'content')

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
