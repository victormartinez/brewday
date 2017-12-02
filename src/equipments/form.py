from django import forms

from src.equipments.models import UserEquipment


class DecreaseUserEquipmentForm(forms.ModelForm):
    class Meta:
        model = UserEquipment
        fields = ['quantity', ]


class NewUserEquipmentForm(forms.ModelForm):
    class Meta:
        model = UserEquipment
        fields = ['equipment', 'quantity', 'capacity', 'unit']


NewUserEquipmentFormSet = forms.modelformset_factory(UserEquipment,
                                                     fields=('equipment', 'quantity', 'capacity', 'unit'), max_num=10)
