from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    # relation
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')

    # data
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200)

    # Date
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Status(models.TextChoices):
        DRAFT = 'DR', 'draft'
        PUBLISHED = 'PB', 'published'
        REJECTED = 'RJ', 'rejected'
    # choices
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published'])
        ]

    def __str__(self):
        return self.title
