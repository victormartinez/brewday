from django import forms

from src.equipments.models import UserEquipment, RecipeEquipment

NewUserEquipmentFormSet = forms.modelformset_factory(
    UserEquipment,
    fields=('equipment', 'quantity', 'capacity', 'unit'),
    exclude=('id',),
    max_num=10,
)

NewRecipeEquipmentFormSet = forms.modelformset_factory(
    RecipeEquipment,
    fields=('equipment', 'quantity', 'capacity', 'unit'),
    exclude=('id',),
    max_num=10,
)
