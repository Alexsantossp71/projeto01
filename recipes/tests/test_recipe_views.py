from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe, User


class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_return_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_show_no_recipies_if_no(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(response.content.decode('utf-8'),
                      'NENHUMA RECEITA CADASTRADA AINDA')

    def recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='password',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(
            title='Recipe Title',
            description='Recipe Description',
            slug='Recipe-Slug',
            preparation_time=10,
            preparation_time_unit='minutos',
            servings=5,
            servings_unit='pessoas',
            preparation_steps='paso de preparacao',
            preparation_steps_is_html=False,
            is_published=True,
            category=category,
            author=author,
        )
        ...

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_return_status_code_200_ok(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_view_return_status_code_404_ok(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)


# URL PA RTE NS NO SETTINGs
