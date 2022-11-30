from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

# Create your tests here.


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


# We're testing that the view functions are correct
class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        # It's taking the url name 'recipes:home' and reversing it to '/'.
        # Then it's resolving that url to the view function.
        # Resolve take the url and return what is the function of that url.
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)
