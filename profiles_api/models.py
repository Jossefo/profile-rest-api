from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    ''' Manager for user profiles'''
    def create_user(self,email,name,password=None):
        '''create new user profile '''
        if not email:
            raise ValueError('user must have email address')
        email = self.normalize_email(email)
        user = self.model(email=email , name=name)
        user.set_password(password) #to hash password
        user.save(using = self._db)
        return user

    def create_super_user(self,email,name,password):
        '''create new super user '''
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True

        return user

class UserProfile (AbstractBaseUser , PermissionsMixin):
    ''' Databse model for users in system '''
    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name']

    def get_full_name (self):
        ''' get full name of user'''
        return self.name

    def get_short_name(self):
        ''' get short name '''
        return self.name

    def __str__(self):
        '''return string of our user'''
        return self.email
