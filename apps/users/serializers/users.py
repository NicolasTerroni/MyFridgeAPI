"""Users serializers"""

# Django
from apps.users.models import User, Profile, Fridge
from django.contrib.auth import authenticate, password_validation

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from rest_framework.authtoken.models import Token

# Serializers
from apps.users.serializers.profiles import ProfileModelSerializer
from apps.users.serializers.fridges import FridgeModelSerializer


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    profile = ProfileModelSerializer(read_only=True)
    fridge = FridgeModelSerializer(read_only=True)

    class Meta:
        """Meta class"""
        model = User
        fields = (
            'id',
            'email',
            'username',
            'is_admin',
            'is_verified',
            'is_active',
            'profile',
            'fridge'
        )


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.
    
    Handle the login request data."""

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'],password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        # For the account verification function:
        # if not user.is_verified:
        #     raise serializers.ValidationError('Account is not active yet.')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer.
    
    Handle sign up data validation and user/profile creation."""

    email = serializers.EmailField(
        validators= [UniqueValidator(queryset=User.objects.all())],
    )
    username = serializers.CharField(
        min_length = 4,
        max_length= 20,
        validators= [UniqueValidator(queryset=User.objects.all())],
    )    
    password = serializers.CharField(min_length=8,max_length=64)
    password_confirmation = serializers.CharField(min_length=8,max_length=64)

    def validate(self, data):
        """Verify password match."""
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise serializers.ValidationError("Passwords didn't match")
        password_validation.validate_password(password)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False) #for the account verification function
        Profile.objects.create(user=user)
        Fridge.objects.create(owner=user)

        # here the confirmation email would be sent, and that would generate an 
        # account verification token, after the account verification, the user would be allowed
        # to do its first login.
        # This has to be a side task.

        return user