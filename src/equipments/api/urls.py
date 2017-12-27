from django.conf.urls import url

from src.equipments.api.views import retrieve_equipment

urlpatterns = [
    url(r'^(?P<pk>[\d]+)$', retrieve_equipment, name='retrieve'),
]
