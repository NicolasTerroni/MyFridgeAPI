"""Recipes views tests"""

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models 
from apps.users.models import User, Fridge
from rest_framework.authtoken.models import Token
from apps.ingredients.models import Ingredient
from apps.recipes.models import Recipe


class TestViews(APITestCase):
    """Recipes views tests"""

    def setUp(self):
        self.user = User.objects.create(
            email="test@email.com",
            username="testuser",
            password="testpass1",
        )
        self.user_fridge = Fridge.objects.create(owner=self.user)

        self.first_ingredient = Ingredient.objects.create(
                    name="first ingredient",
                    slug_name="first_ingredient",
                    created_by=self.user,
                    description="first_ingredient",
                    is_veggie=True,
                    is_vegan=True
        )
        self.second_ingredient = Ingredient.objects.create(
                    name="second ingredient",
                    slug_name="second_ingredient",
                    created_by=self.user,
                    description="second_ingredient",
                    is_veggie=True,
                    is_vegan=True
        )
        self.third_ingredient = Ingredient.objects.create(
                    name="third ingredient",
                    slug_name="third_ingredient",
                    created_by=self.user,
                    description="third_ingredient",
                    is_veggie=True,
                    is_vegan=True
        )
        self.recipe = Recipe.objects.create(
            name="test recipe",
            slug_name="test_recipe",
            created_by=self.user
        )
        self.recipe.ingredients.set([self.first_ingredient.id,self.second_ingredient.id])

        # Auth
        self.token = Token.objects.create(user=self.user).key
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        # URLs
        self.recipes_url = "/recipes/"
        self.recipes_slug_url = f"/recipes/{self.recipe.slug_name}/"
        self.possible_recipes_url = "/recipes/possible_recipes/"
        self.my_recipes_url = "/recipes/my_recipes/"


    def test_recipe_creation(self):
        response = self.client.post(
            self.recipes_url,
            {
                "name": "Mashed potatoes",
                "slug_name": "mashed_potatoes",
                "ingredients":[f"{self.first_ingredient.id}",f"{self.second_ingredient.id}"]
            },
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['slug_name'], 'mashed_potatoes')
        self.assertEqual(response.data['created_by'], self.user.username)
        self.assertEqual(Recipe.objects.all().count(), 2)

    def test_list_recipes(self):
        response = self.client.get(self.recipes_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], Recipe.objects.all().count())

    def test_recipe_detail(self):
        response = self.client.get(self.recipes_slug_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['slug_name'], self.recipe.slug_name)

    def test_update_recipe(self):
        previous_ingredients = [self.first_ingredient, self.second_ingredient]
        response = self.client.put(
            self.recipes_slug_url,
            {
                "name": "Mashed potatoes",
                "slug_name": "mashed_potatoes",
                "ingredients":[f"{self.third_ingredient.id}",f"{self.second_ingredient.id}"]
            },
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(
            previous_ingredients, 
            Recipe.objects.get(slug_name="mashed_potatoes").ingredients.all()
        )
        self.assertEqual(Recipe.objects.all().count(), 1)

    def test_partial_update_recipe(self):
        previous_ingredients = [self.first_ingredient, self.second_ingredient]
        response = self.client.patch(
            self.recipes_slug_url,
            {
                "ingredients":[f"{self.third_ingredient.id}",f"{self.second_ingredient.id}"]
            },
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(
            previous_ingredients, 
            Recipe.objects.get(slug_name=self.recipe.slug_name).ingredients.all()
        )
        self.assertEqual(Recipe.objects.all().count(), 1)

    def test_delete_recipe(self):
        response = self.client.delete(self.recipes_slug_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(response.data)
        self.assertEqual(Recipe.objects.all().count(), 0)

    def test_list_fridge_ingredients_recipes(self):
        # Add an ingredient to user's fridge
        self.user_fridge.ingredients.set([self.third_ingredient.id,])
        # Create a recipe that contain the user fridge ingredient
        user_possible_recipe = Recipe.objects.create(
            name="user fridge recipe",
            slug_name="user_fridge_recipe",
            created_by=self.user
        )
        user_possible_recipe.ingredients.set([self.third_ingredient.id,self.second_ingredient.id])
        # Our setUp recipe does not contain the user fridge ingredient
        response = self.client.get(self.possible_recipes_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.third_ingredient, user_possible_recipe.ingredients.all())
        self.assertIn(self.third_ingredient, self.user.fridge.ingredients.all())
        self.assertEqual(response.data['count'], 1)
        # Just 'user_possible_recipe', setUp recipe must not be returned

    def test_list_user_recipes(self):
        Recipe.objects.create(
            name="second recipe",
            slug_name="second_recipe",
            created_by=self.user
        )
        Recipe.objects.create(
            name="third recipe",
            slug_name="third_recipe"
        )
        response = self.client.get(self.my_recipes_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['count'], 
            Recipe.objects.filter(created_by=self.user).count()
        )

