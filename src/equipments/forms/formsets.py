from django import forms

from src.equipments.models import UserEquipment

NewUserEquipmentFormSet = forms.modelformset_factory(
    UserEquipment,
    fields=('equipment', 'quantity', 'volume_capacity', 'weight_capacity'),
    exclude=('id',),
    max_num=10,
)
