from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views
from recipes.models import Category, Recipe


class RecipeViewsTest(TestCase):
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
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='User',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.co,',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings_time=5,
            servings_time_unit='porçoes',
            preparation_step='Recipe Preparation Steps',
            preparation_step_is_html=False,
            is_published=True,
        )
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn('Recipe Title', content)

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

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)
