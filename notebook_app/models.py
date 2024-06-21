from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    NOTE_TYPES = (
        ('normal', 'Normal'),
        ('todo', 'To-Do'),
        ('checklist', 'Checklist'),
        ('other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200)
    content = models.TextField()
    note_type = models.CharField(max_length=20, choices=NOTE_TYPES, default='normal')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ChecklistItem(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='checklist_items')
    text = models.CharField(max_length=200)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.text
