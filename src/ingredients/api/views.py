from rest_framework.generics import RetrieveAPIView

from src.ingredients.api.serializers import IngredientTypeSerializer
from src.ingredients.models import IngredientType


class IngredientTypeRetrieveView(RetrieveAPIView):
    serializer_class = IngredientTypeSerializer
    queryset = IngredientType.objects.all()


retrieve_ingredient_type = IngredientTypeRetrieveView.as_view()
