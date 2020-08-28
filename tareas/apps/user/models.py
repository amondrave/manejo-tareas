from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

""""
Create class user manager for apply methods of create user and super_user
"""


class UserManager(BaseException):
    def create_user(self, email, username, name, password=None):
        if not email:
            raise ValueError('El usuario debe tener un  correo electronico')
        user = self.model(username=username, email=self.normalize_email(
            email), name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, name, password):
        user = self.create_user(
            email, username=username, name=name, password=password)
        user.user_manager = True
        user.save()
        return user


"""
We create the custom user class using AbstractBaseUser inheritance
this class has some attributes that are specific to our database model and some are overwritten from the django user class
"""


class User(AbstractBaseUser):
    username = models.CharField('username', max_length=50, unique=True)
    email = models.EmailField('email', unique=True, max_length=250)
    date_entry = models.DateField(auto_now_add=True)
    name = models.CharField('name', max_length=200, blank=False, null=False)
    dir_image = models.FileField(
        upload_to='imagenes/', max_length=250, null=True, blank=True)
    user_active = models.BooleanField(default=True)
    user_manager = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return "{}".format(self.username)

    def has_perm(self, perm, object=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.user_manager
