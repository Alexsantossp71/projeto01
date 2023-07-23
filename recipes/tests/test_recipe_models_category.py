from recipes.models import Recipe
from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name='111'
        )
        return super().setUp()

    def test_recipe_category_model_string_representation(self):

        self.assertEqual(
            str(self.category),
            self.category.name, msg=f' 1 é {str(self.category)} e 2 é {self.category.name}'
        )

    def test_recipe_category_model_name_is_65_chars(self):
        self.category.name = 'a'*66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
