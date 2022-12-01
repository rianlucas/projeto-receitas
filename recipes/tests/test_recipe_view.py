from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views
from recipes.models import Category, Recipe, User

# We're testing that the view functions are correct


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        # It's taking the url name 'recipes:home' and reversing it to '/'.
        # Then it's resolving that url to the view function.
        # Resolve get the url and return what is the function of that url.
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    # ! The DataBase of test is different from the DataBase of the system
    # ! This tests will fail, to make that pass we should add recipes
    # ! to Test DataBase.
    def test_recipe_category_view_returns_status_code_200_OK(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_templates(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):  # noqa
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No Recipes Yet :/',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='user name',
            password='123',
            email='user@email.com',
        )
        recipe = Recipe.objects.create(  # noqa: F841
            category=category,
            author=author,
            title='Recipe Title',
            description='recipe descricao',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='min',
            servings=5,
            servings_unit='porções',
            preparation_steps='recipe preparation_steps',
            preparation_steps_is_html=False,
            is_published=True,
        )
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        self.assertIn('Recipe Title', content)
        self.assertIn('10 min', content)
        self.assertIn('5 porções', content)
        self.assertEqual(len(response_context_recipes), 1)
