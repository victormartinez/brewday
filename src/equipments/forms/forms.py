from django import forms

from toolz import dicttoolz

from src.equipments.models import UserEquipment


class NewUserEquipmentForm(forms.ModelForm):
    class Meta:
        model = UserEquipment
        fields = ('equipment', 'quantity', 'volume_capacity',)


def create_user_equipments(formset, user):
    cleaned_data_list = list(formset.cleaned_data)

    object_list = []
    for data in cleaned_data_list:
        object_attributes = dicttoolz.merge(data, {'user': user})
        object_list.append(UserEquipment(**object_attributes))

    return UserEquipment.objects.bulk_create(object_list)
