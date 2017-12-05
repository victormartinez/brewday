from django.contrib import admin

from src.equipments.models import Equipment, UserEquipment, RecipeEquipment

admin.site.register(Equipment)
admin.site.register(UserEquipment)
admin.site.register(RecipeEquipment)
