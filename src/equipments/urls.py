from django.conf.urls import url

from .views import (
    my_equipments,
    delete_equipment,
    edit_equipment,
    new_equipment
)

urlpatterns = [
    url(r'^$', my_equipments, name='my'),
    url(r'^new$', new_equipment, name='new'),
    url(r'^(?P<pk>[\w-]+)/edit$', edit_equipment, name='edit'),
    url(r'^(?P<pk>[\w-]+)$', delete_equipment, name='delete'),
]
