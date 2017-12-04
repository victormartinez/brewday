from django import forms

from src.recipes.models import Recipe


class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'expected_quantity', 'og', 'fg', 'ibu', 'srm', 'abv', 'steps', 'observations']
