from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images', verbose_name='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    
    
    def __str__(self):
        return self.user.username
    


