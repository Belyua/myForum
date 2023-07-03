from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    username = models.CharField(max_length=21)
    email = models.EmailField(unique=True, null=False, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    #
    # class Meta:
    #     db_table = "User"


class Topic(models.Model):
    topic_link = models.CharField(max_length=253, null=True, blank=True)
    subject = models.CharField(max_length=253, null=True, blank=True)
    section = models.CharField(max_length=253, null=True, blank=True)
    username = models.CharField(max_length=29)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    content = models.TextField(max_length=253, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.topic_link

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.author.username
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

