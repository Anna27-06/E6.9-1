from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model()


class Room(models.Model):
    name = models.CharField(max_length=256, unique=True)


class CustomUser(AbstractUser):
    name = models.CharField(max_length=256, unique=True)
    avatar = models.ImageField(default='default.png', upload_to='media')
    room = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True)
    USERNAME_FIELD = 'username'

    @staticmethod
    def user_list():
        users = User.objects.all().order_by('name')
        return list(users)


class Message(models.Model):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(Room, on_delete=models.CASCADE)
    room = models.ForeignKey(User, on_delete=models.CASCADE)




