from django.contrib import admin

from src.ingredients.models import IngredientType, RecipeIngredient, UserIngredient

admin.site.register(IngredientType)
admin.site.register(RecipeIngredient)
admin.site.register(UserIngredient)
