from django.conf.urls import url

from .views import new_recipe

urlpatterns = [
    url(r'^new$', new_recipe, name='new'),
]
