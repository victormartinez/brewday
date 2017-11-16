from django.conf.urls import url

from .views import my_storage, new_ingredient

urlpatterns = [
    url(r'^$', my_storage, name='my'),
    url(r'^new-ingredient$', new_ingredient, name='new_ingredient'),
]
