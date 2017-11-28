from django import forms
from django.forms import modelformset_factory

from src.ingredients.models import UserIngredient


class NewUserIngredientForm(forms.ModelForm):
    class Meta:
        model = UserIngredient
        fields = ['name', 'quantity', 'unit']


NewUserIngredientFormSet = modelformset_factory(UserIngredient, fields=('name', 'quantity', 'unit'), max_num=10)
