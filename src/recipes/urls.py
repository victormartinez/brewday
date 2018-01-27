from django.conf.urls import url

from .views import (
    new_recipe,
    my_recipes,
    show_recipe,
    edit_recipe,
    delete_recipe,
    new_batch,
    suggest_view
)

urlpatterns = [
    url(r'^my-recipes$', my_recipes, name='my'),
    url(r'^new$', new_recipe, name='new'),
    url(r'^suggest$', suggest_view, name='suggest'),
    url(r'^(?P<pk>[\d]+)/edit$', edit_recipe, name='edit'),
    url(r'^(?P<pk>[\d]+)/delete$', delete_recipe, name='delete'),
    url(r'^(?P<pk>[\d]+)/batch$', new_batch, name='new_batch'),
    url(r'^(?P<pk>[\d]+)$', show_recipe, name='show'),
]
