from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from utils.validators import validate_email, validate_password, validate_first_name, validate_last_name


class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Email is required")
        if not first_name or not last_name:
            raise ValueError("First name and last name are required")
        validate_email(email)
        validate_first_name(first_name)
        validate_last_name(last_name)
        if password:
            validate_password(password)

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Email is required")
        if not first_name or not last_name:
            raise ValueError("First name and last name are required")
        validate_email(email)
        validate_first_name(first_name)
        validate_last_name(last_name)
        if password:
            validate_password(password)

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

