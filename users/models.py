from django.db import models

# Create your models here.
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyUserManager(BaseUserManager):
   def create_user(self, username,password=None):
       """
       Creates and saves a User with the given email,and password.
       """
       if not username:
           raise ValueError('Users must have an email address')
 
       user = self.model(username=username)
       user.set_password(password)
       user.save(using=self._db)
       return user
 
   def create_superuser(self, username,password=None):
       """
       Creates and saves a superuser with the given email, date of
       birth and password.
       """
       user = self.create_user(username,password=password)
       user.is_admin = True
       user.save(using=self._db)
       return user
 

class User(AbstractBaseUser):
    username = models.CharField(max_length=100,unique=True,)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True