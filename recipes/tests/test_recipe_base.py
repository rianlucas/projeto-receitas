from django.test import TestCase

from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_recipe_no_default(self):
        recipe = Recipe(
            category=self.make_category(name='Teste Default Category'),
            author=self.make_author(username='NewUser'),
            title='Recipe Title',
            description='recipe descricao',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='min',
            servings=5,
            servings_unit='porções',
            preparation_steps='recipe preparation_steps',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(self,
                    first_name='user',
                    last_name='name',
                    username='user name',
                    password='123',
                    email='user@email.com',
                    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )

    def make_recipe(
        self,
        category_data=None,
        author_data=None,
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
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(  # noqa: F841
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
        )
