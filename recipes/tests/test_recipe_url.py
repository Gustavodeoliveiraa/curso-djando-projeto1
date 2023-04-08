from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_recipe_home_urls_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_urls_is_correct(self):
        url = reverse('recipes:category', kwargs={"category_id": 1})
        self.assertEqual(url, '/recipes/category/1/')

    def teste_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', args=(1,))
        self.assertEqual(url, "/recipes/1/")
