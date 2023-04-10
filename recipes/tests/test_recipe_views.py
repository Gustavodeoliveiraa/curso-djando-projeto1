from unittest import skip

from django.urls import resolve, reverse

from recipes import views

from .teste_recipe_base import RecipeTestCase


class RecipeViewsTest(RecipeTestCase):
    def teste_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')


    def test_recipe_home_template_show_no_recipe_founds_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8')
            )

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipe = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipe), 1)

    def teste_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={"category_id": 1})
        )

        self.assertIs(view.func, views.category)

    def teste_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 100})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipe_category_views_returns_404_if_no_recipe_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)
