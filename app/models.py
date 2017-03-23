from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser 
)

class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            date_of_birth = date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, date_of_birth, password):
        #Create and save a superuser with the given email, date of birth and password 
        user = self.create_user(
            email,
            password = password,
            date_of_birth = date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']
    ''' has_perm, has_module_perms and is_staff just used to Compatible with django framework'''
    def get_full_name(self):
        # The user is identified by their email address
        return self.email
    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    def __str__(self): # __unicode__ on Python 2
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_lable):
        '''Does the user have permissions to view the app `app_label`?'''
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        ''' Is the user a member of staff? '''
        return self.is_admin
   """   Blog  relevant model """

class Blog (models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author( models.Model ):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry( models.Model ):
    blog = models.ForeignKey( Blog )
    headline = models.CharField( max_length=255 )
    body__text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField( Author )
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
