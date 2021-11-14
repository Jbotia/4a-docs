
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .rol import Rol

class UserManager(BaseUserManager): ##user manager, hereda de baseUserManager
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    name  = models.CharField('name', max_length = 30)
    last_name = models.CharField('last_name', max_length=45,default ='')#Validar, requirio default
    cedula = models.CharField('cedula',max_length=20,unique=True,default ='') #Validar, requirio default
    create_time = models.DateTimeField('dateTime', default=datetime.now, blank=True)
    email = models.EmailField('Email', max_length = 100)
    rol = models.ForeignKey(Rol,related_name='rol_Usuario', on_delete = models.CASCADE)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN' 
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'