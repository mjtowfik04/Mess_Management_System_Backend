from django.db import models
from django.contrib.auth.models import AbstractUser
from Users.managers import CustomUserManager

class User(AbstractUser):
    username=None
    email= models.EmailField(unique=True)
    address=models.CharField(max_length=20,blank=None,null=True)
    Phone=models.CharField(max_length=12,blank=None,null=True)


    USERNAME_FIELD='email'

    REQUIRED_FIELDS=[]
    objects=CustomUserManager()

    def __str__(self):
        return self.email
