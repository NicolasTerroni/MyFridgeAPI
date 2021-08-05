"""Users views tests"""

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models 
from apps.users.models import User, Profile, Fridge
from rest_framework.authtoken.models import Token
from apps.ingredients.models import Ingredient

class TestNoAuthViews(APITestCase):
    """Users sign up and login tests."""

    def setUp(self):

        self.user_data = {
            "email": "test@email.com",
            "username": "testuser",
            "password": "testpass1",
            "password_confirmation": "testpass1",
        }
        # URLs
        self.signup_url = "/users/signup/"
        self.login_url = "/users/login/"

    def test_cant_signup(self):
        # Cant sign up without data
        response = self.client.post(self.signup_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup(self):
        response = self.client.post(
            self.signup_url, 
            self.user_data, 
            format="json"
        )
        # Ensure request data was sent
        self.assertEqual(response.data['email'], self.user_data['email'])
        self.assertEqual(response.data['username'], self.user_data['username'])
        # Ensure fridge and profile where created
        self.assertIsInstance(response.data['profile'], dict)
        self.assertIsInstance(response.data['fridge'], dict)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cant_login(self):
        # Sign up to create a user correctly
        self.client.post(
            self.signup_url, 
            self.user_data, 
            format="json"
        )
        # Ensure user can't login without sending data
        response = self.client.post(self.login_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Ensure user can't login with invalid credentials
        response = self.client.post(
            self.login_url, 
            {
                "email": "test@email.com", 
                "password": "bad_password"
            },
            format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        # Sign up to create a user correctly
        self.client.post(
            self.signup_url, 
            self.user_data, 
            format="json"
        )
        # Sign in
        response = self.client.post(
            self.login_url, 
            {
                "email": f"{self.user_data['email']}", 
                "password": f"{self.user_data['password']}"
            },
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Ensure token was created correctly
        self.assertEqual(response.data['access_token'], Token.objects.first().key)


class TestAuthRequiredViews(APITestCase):
    """User detail, update and partial update tests"""

    def setUp(self):
        self.user = User.objects.create(
            email="test@email.com",
            username="testuser",
            password="testpass1",
        )
        self.profile = Profile.objects.create(user=self.user)
        self.fridge = Fridge.objects.create(owner=self.user)

        # Auth
        self.user_token = Token.objects.create(user=self.user).key
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_token}')

        # Ingredient to test the fridge update
        self.ingredient = Ingredient.objects.create(
            name="test_ingredient",
            slug_name="test",
            description="test ingredient",
            is_veggie=True,
            is_vegan=True
        )
        # URLs
        self.detail_url = f"/users/{self.user.username}/"
        self.update_url = f"/users/{self.user.username}/"
        self.profile_url = f"/users/{self.user.username}/profile/"
        self.fridge_url = f"/users/{self.user.username}/fridge/"
        

    def test_user_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user(self):
        response = self.client.put(
            self.update_url,
            {
                "email": "updated_email@gmail.com",
                "username": "updated_username"
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'updated_email@gmail.com')
        self.assertEqual(response.data['username'], 'updated_username')

    def test_partial_update_user(self):
        response = self.client.patch(
            self.update_url,
            {
                "username": "partial_updated_username"
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'partial_updated_username')
        
    def test_update_profile(self):
        response = self.client.put(
            self.profile_url,
            {
                "first_name": "updated_first_name",
                "last_name": "updated_last_name",
                "biography": "updated biography"
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['profile']['last_name'], 'updated_last_name')

    def test_partial_update_profile(self):
        response = self.client.patch(
            self.profile_url,
            {
                "last_name": "updated_last_name"
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['profile']['last_name'], 'updated_last_name')

    def test_partial_update_fridge(self):
        response = self.client.patch(
            self.fridge_url,
            {
                "ingredients":[f"{self.ingredient.id}"]
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['fridge']['ingredients'], [self.ingredient.id])
