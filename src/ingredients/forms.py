from django import forms
from django.forms import modelformset_factory, inlineformset_factory

from src.ingredients.models import UserIngredient, RecipeIngredient
from src.recipes.models import Recipe


class NewUserIngredientForm(forms.ModelForm):
    class Meta:
        model = UserIngredient
        fields = ['name', 'ingredient_type', 'volume_quantity', 'weight_quantity']


NewUserIngredientFormSet = modelformset_factory(UserIngredient, fields=('name', 'ingredient_type', 'volume_quantity', 'weight_quantity'), max_num=10)
NewRecipeIngredientFormSet = modelformset_factory(RecipeIngredient, fields=('name', 'ingredient_type', 'volume_quantity', 'weight_quantity'), max_num=20, extra=0)
EditRecipeIngredientFormSet = inlineformset_factory(Recipe, RecipeIngredient, fields=('name', 'ingredient_type', 'volume_quantity', 'weight_quantity'), max_num=20)

