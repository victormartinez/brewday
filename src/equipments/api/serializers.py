from rest_framework.serializers import ModelSerializer

from src.equipments.models import Equipment


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('name', 'is_measured',)
