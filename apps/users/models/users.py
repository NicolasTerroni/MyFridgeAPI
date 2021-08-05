"""User model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Utilities
from apps.utils.models import TimeStamp


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, *args, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('The given username must be set')
            
        user = self.model(email=self.normalize_email(email),username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, TimeStamp):
    """Custom user model.
    
    Extends from Django's AbstractUser and our TimeStamp.
    Changes username field to email and adds some extra fields.
    """
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique':'A user with that email already exists.'
        },
        max_length=254)
    
    username = models.CharField(
        max_length=30,
        unique=True,
        help_text=('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    REQUIRED_FIELDS = ('username',)
    USERNAME_FIELD = 'email'

    is_admin = models.BooleanField(default=False)

    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    # this is for a future account verification function
    is_verified = models.BooleanField(
        'is_verified',
        default=False,
        help_text=(
            'Set to True when the user have verified its email address.'
        ),
    )
    objects = UserManager()

    def __str__(self):
        """Return username"""
        return self.username

    def get_short_name(self):
        """Return username"""
        return self.username   

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

