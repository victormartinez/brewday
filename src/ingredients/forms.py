from django import forms
from django.forms import modelformset_factory

from src.ingredients.models import UserIngredient, RecipeIngredient


class IncreaseUserIngredientForm(forms.ModelForm):
    amount = forms.IntegerField()

    class Meta:
        model = UserIngredient
        fields = ['quantity', 'amount']

    def save(self, commit=True):
        amount = self.cleaned_data['amount']
        self.instance.increase(amount)
        self.instance.save()
        return self.instance


class DecreaseUserIngredientForm(forms.ModelForm):
    amount = forms.IntegerField()

    class Meta:
        model = UserIngredient
        fields = ['quantity', 'amount']

    def save(self, commit=True):
        amount = self.cleaned_data['amount']
        self.instance.decrease(amount)
        self.instance.save()
        return self.instance


class NewUserIngredientForm(forms.ModelForm):
    class Meta:
        model = UserIngredient
        fields = ['name', 'quantity', 'unit']


NewUserIngredientFormSet = modelformset_factory(UserIngredient, fields=('name', 'quantity', 'unit'), max_num=10)
NewRecipeIngredientFormSet = modelformset_factory(RecipeIngredient, fields=('name', 'quantity', 'unit'), max_num=20)
