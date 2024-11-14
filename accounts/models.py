from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user_avatar = models.ImageField(default='default.jpg', upload_to='profile_images', verbose_name='Foto Perfil')
    user_fname = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_fname', verbose_name='Primeiro Nome')
    user_lname = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_lname', verbose_name='Último Nome')
    
    def __str__(self):
        return self.userusername
    


