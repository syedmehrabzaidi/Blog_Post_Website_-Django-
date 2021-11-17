from django.contrib.auth.models import User
from django.db import models


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    follower = models.ManyToManyField(User, related_name='follower_r', blank=True, symmetrical=False)
    following = models.ManyToManyField(User, related_name='following_r', blank=True, symmetrical=False)
    bio = models.TextField(default='no bio .....')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ('-created_at',)
