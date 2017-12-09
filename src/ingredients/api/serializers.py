from rest_framework.serializers import ModelSerializer

from src.ingredients.models import IngredientType


class IngredientTypeSerializer(ModelSerializer):
    class Meta:
        model = IngredientType
        fields = ('name', 'measured_by',)
