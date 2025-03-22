from django.db import models

class Mentorship(models.Model):
    # other fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # auto-updating field
    
    # other fields and methods
