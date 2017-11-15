from django.conf.urls import url

from .views import new_recipe, my_recipes

urlpatterns = [
    url(r'^my-recipes$', my_recipes, name='my_recipes'),
    url(r'^new$', new_recipe, name='new'),
]