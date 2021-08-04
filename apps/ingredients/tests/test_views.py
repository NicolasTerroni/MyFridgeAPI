"""Ingredients views tests"""

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models 
from apps.users.models import User
from rest_framework.authtoken.models import Token
from apps.ingredients.models import Ingredient


class TestViews(APITestCase):
    """Ingredients CRUD tests"""

    def setUp(self):
        self.user = User.objects.create(
            email="test@email.com",
            username="testuser",
            password="testpass1",
        )
        self.ingredient = Ingredient.objects.create(
                    name="test_ingredient",
                    slug_name="test",
                    created_by=self.user,
                    description="test ingredient",
                    is_veggie=True,
                    is_vegan=True
        )
        # Auth
        self.token = Token.objects.create(user=self.user).key
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        # URLs
        self.ingredients_url = "/ingredients/"
        self.ingredients_slug_url = f"/ingredients/{self.ingredient.slug_name}/"

    def test_ingredient_creation(self):
        
        response = self.client.post(
            self.ingredients_url,
            {
                "name": "Nutmeg",
                "slug_name": "numteg",
                "description": "Nutmeg",
                "is_veggie": True,
                "is_vegan": True
            },
            format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingredient.objects.count(), 2) # setUp ingredient + this one
        self.assertEqual(response.data['name'], "Nutmeg")
        self.assertEqual(response.data['created_by'], self.user.username)

    def test_list_ingredients(self):
        response = self.client.get(self.ingredients_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], Ingredient.objects.all().count())

    def test_ingredient_detail(self):
        response = self.client.get(self.ingredients_slug_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_ingredient(self):
        response = self.client.put(
            self.ingredients_slug_url,
            {
                "name": "Apples",
                "slug_name": "apples",
                "is_veggie": True,
                "is_vegan": True
            },
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['slug_name'], 'apples')
        self.assertEqual(Ingredient.objects.all().count(), 1)

    def test_partial_update_ingredient(self):
        response = self.client.patch(
            self.ingredients_slug_url,
            {
                "name": "Apples"
            },
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Apples')
        self.assertEqual(response.data['slug_name'], self.ingredient.slug_name)
        self.assertEqual(Ingredient.objects.all().count(), 1)

    def test_delete_ingredient(self):
        response = self.client.delete(self.ingredients_slug_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(response.data)
        self.assertEqual(Ingredient.objects.all().count(), 0)






#import ipdb; ipdb.set_trace()
