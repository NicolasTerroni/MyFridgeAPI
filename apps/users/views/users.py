"""Users views."""

# Django REST Framework
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework import status

# Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.users import serializers
from apps.users.permissions import IsAccountOwner

# Models
from apps.users.models import User

# Serializers
from apps.users.serializers import (UserLoginSerializer, 
                                    UserModelSerializer, 
                                    UserSignUpSerializer, 
                                    ProfileModelSerializer)


class UserViewSet(RetrieveModelMixin,UpdateModelMixin,GenericViewSet):
    """User model viewset."""

    queryset = User.objects.all() # is_active=True
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on actions."""
        if self.action in ['signup','login']:  # ,'verify'
            permissions = [AllowAny]
        elif self.action in ['retrieve','update','partial_update','profile']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request, *args, **kwargs):
        """Handle user login request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token,
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request, *args, **kwargs):
        """Handle user sign up request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=True,methods=['put','patch'])
    def profile(self, request, *args, **kwargs):
        """Handle user's profile update and partial update."""
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH' 
        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)



"""
    @action(detail=False, methods=['post'])
    def verify(self,request):
        'User account verification.'
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': 'Your account is active now.',
        }
        return Response(data, status=status.HTTP_200_OK) 
"""