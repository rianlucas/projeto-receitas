from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase

# We're testing that the view functions are correct


class RecipeDetailViewTest(RecipeTestBase):

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': recipe.id
                }
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_correct_recipes(self):
        self.make_recipe()

        response = self.client.get(reverse('recipes:recipe', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn('Recipe Title', content)
