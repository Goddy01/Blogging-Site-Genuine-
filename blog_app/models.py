import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name='email address', max_length=50, unique=True)
    username        = models.CharField(unique=True, max_length=25)
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_supersuer    = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f"Username: {self.username} Email: {self.email}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self):
        return True