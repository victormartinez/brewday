from django import forms

from src.equipments.models import UserEquipment, RecipeEquipment

# TODO: Rename this module to forms.
class NewUserEquipmentForm(forms.ModelForm):
    class Meta:
        model = UserEquipment
        fields = ['equipment', 'quantity', 'capacity', 'unit']


NewUserEquipmentFormSet = forms.modelformset_factory(UserEquipment,
                                                     fields=('equipment', 'quantity', 'capacity', 'unit'), max_num=10)

NewRecipeEquipmentFormSet = forms.modelformset_factory(RecipeEquipment, fields=('equipment', 'quantity', 'capacity', 'unit'), max_num=10)
