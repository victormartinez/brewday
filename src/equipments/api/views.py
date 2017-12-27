from rest_framework.generics import RetrieveAPIView

from src.equipments.api.serializers import EquipmentSerializer
from src.equipments.models import Equipment


class EquipmentRetrieveView(RetrieveAPIView):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()


retrieve_equipment = EquipmentRetrieveView.as_view()
