from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser 
)

class UserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            date_of_birth = date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=20)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth']
    
