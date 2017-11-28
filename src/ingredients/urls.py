from django.conf.urls import url

from .views import (
    my_ingredients,
    new_ingredient,
    delete_ingredient,
    increase_ingredient,
    decrease_ingredient,
    edit_ingredient
)

urlpatterns = [
    url(r'^$', my_ingredients, name='my'),
    url(r'^new$', new_ingredient, name='new'),
    url(r'^(?P<pk>[\w-]+)/edit$', edit_ingredient, name='edit'),
    url(r'^(?P<pk>[\w-]+)/increase$', increase_ingredient, name='increase'),
    url(r'^(?P<pk>[\w-]+)/decrease$', decrease_ingredient, name='decrease'),
    url(r'^(?P<pk>[\w-]+)$', delete_ingredient, name='delete'),
]
