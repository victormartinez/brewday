from django.conf.urls import url

from src.ingredients.api.views import retrieve_ingredient_type

urlpatterns = [
    url(r'^(?P<pk>[\d]+)$', retrieve_ingredient_type, name='retrieve'),
]
