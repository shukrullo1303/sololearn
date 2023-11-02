from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    xp = models.PositiveIntegerField(default=0, null=True, blank=True)    
    user_picture = models.ImageField(blank=True, null=True, upload_to="imgs/profile_pics/")


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ("Foydalanuvchi ")
        verbose_name_plural = ("Foydalanuvchilar")