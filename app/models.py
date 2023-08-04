from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractUser):
    pass 

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey('Blog', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(default="...")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.content}"

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])