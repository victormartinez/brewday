from django.conf.urls import url

from .views import my_ingredients, new_ingredient

urlpatterns = [
    url(r'^$', my_ingredients, name='my'),
    url(r'^new$', new_ingredient, name='new'),
]
