from django.test import TestCase
from django.urls import reverse


# We're testing that the urls for our recipes app are correct
class RecipeUrlsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        recipe_url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(recipe_url, '/recipes/1/')
