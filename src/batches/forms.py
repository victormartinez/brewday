from django import forms
from django.core.exceptions import ValidationError

from src.batches.models import RecipeBatch
from src.equipments.models import UserEquipment

EQUIPMENTS_REQUIRED = 'mash-tun', 'lauter-tun', 'boiling-kettle', 'hot-liquor-tank'


class NewRecipeBatchForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')

        self._validate_user_has_minimum_equipments(user)
        self._validate_user_has_available_equipments(user)

        return cleaned_data

    def _validate_user_has_minimum_equipments(self, user):
        user_equipments = UserEquipment.objects.filter(user=user, equipment__slug__in=EQUIPMENTS_REQUIRED)
        if len(EQUIPMENTS_REQUIRED) != user_equipments.count():
            raise ValidationError('You do not have the minimum equipments to start a batch. You need, at least, '
                                  '1 Mash Tun, 1 Lauter Tun, 1 Boiling Kettle, 1 Hot Liquor Tank')

    def _validate_user_has_available_equipments(self, user):
        pass

    class Meta:
        model = RecipeBatch
        fields = ['recipe', 'user']
