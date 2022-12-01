from django.test import TestCase

from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
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
        return super().setUp()
