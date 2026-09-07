from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    tags = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User,
        related_name='liked_photos',
        blank=True
    )
    dislikes = models.ManyToManyField(
        User,
        related_name='disliked_photos',
        blank=True
    )

    def __str__(self):
        return self.title