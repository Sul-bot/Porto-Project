from audioop import reverse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User



class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
            

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    data_joined = models.DateTimeField(verbose_name='data joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    

class Image(models.Model):
    WEDDING = 'wedding'
    PARTY = 'party'
    EVENT = 'event'
    BIRTHDAY = 'birthday'

    IMAGE_TYPES = [
        (WEDDING, 'Wedding'),
        (PARTY, 'Party'),
        (EVENT, 'Event'),
        (BIRTHDAY, 'Birthday'),
    ]

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPES, default=WEDDING)  # Contoh default di sini

    def __str__(self):
        return self.title


    def __str__(self):
        return self.title

    

class Card(models.Model):
    message = models.CharField(max_length=450)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name



    
    
    
