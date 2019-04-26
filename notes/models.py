"""Note Models"""

# Django
from django.db import models


class Note(models.Model):
    """Note model."""

    title = models.CharField(max_length=150)
    content = models.TextField()
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

