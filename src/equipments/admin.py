from django.contrib import admin

from src.equipments.models import Equipment, UserEquipment

admin.site.register(Equipment)
admin.site.register(UserEquipment)
