"""Users views."""

# Django REST Framework
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status

# Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.users.permissions import IsAccountOwner

# Models
from apps.users.models import User

# Serializers
from apps.users.serializers import UserLoginSerializer, UserModelSerializer, UserSignUpSerializer

class UserViewSet(viewsets.ModelViewSet):
    """User  model viewset."""

    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'email'

    def get_permissions(self):
        """Assign permissions based on actions."""
        if self.action in ['signup','login']:  # ,'verify'
            permissions = [AllowAny]
        # elif self.action in ['retrieve','update','partial_update','profile']:
        #    permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]    
        return [permission() for permission in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request, *args, **kwargs):
        "Handle user login request."
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
        "Handle user sign up request."
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
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
            'message': 'Congratulations, now go share some rides!',
        }
        return Response(data, status=status.HTTP_200_OK) 
"""