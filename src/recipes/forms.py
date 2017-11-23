from django import forms

from src.recipes.models import Recipe


class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'og', 'fg', 'ibu', 'srm', 'abv', 'steps', 'observations']

    def __init__(self, *args, **kwargs):
        super(NewRecipeForm, self).__init__(*args, **kwargs)
        # self.fields['unit'].choices = UNIT_CHOICES
