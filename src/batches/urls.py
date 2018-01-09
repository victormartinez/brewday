from django.conf.urls import url

from .views import my_batches

urlpatterns = [
    url(r'^$', my_batches, name='my'),
]
