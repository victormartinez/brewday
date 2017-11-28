from django import forms
from django.utils.translation import gettext as _
from django.forms import modelformset_factory

from src.ingredients.models import UserIngredient, RecipeIngredient


class IncreaseUserIngredientForm(forms.ModelForm):
    amount = forms.IntegerField()

    class Meta:
        model = UserIngredient
        fields = ['quantity', 'amount']

    def clean_amount(self):
        amount = self.data['amount']
        if int(amount) == 0:
            raise forms.ValidationError(
                _('The amount must be greater than zero.'),
                code='invalid',
            )

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

    def clean_amount(self):
        amount = self.data['amount']
        if int(amount) == 0:
            raise forms.ValidationError(
                _('The amount must be greater than zero.'),
                code='invalid',
            )

        if not self.instance.can_decrease_by(int(amount)):
            raise forms.ValidationError(
                _('The current quantity (%(quantity)s) corresponds to less than the amount decreased.'),
                code='invalid',
                params={'quantity': self.instance.quantity}
            )

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
