from django import forms

from src.ingredients.models import UserIngredient


class NewIngredientForm(forms.ModelForm):
    class Meta:
        model = UserIngredient
        fields = ['name', 'quantity', 'unit']
