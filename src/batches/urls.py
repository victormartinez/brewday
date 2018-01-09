from django.conf.urls import url

from .views import my_batches, finish_batch, restart_batch

urlpatterns = [
    url(r'^$', my_batches, name='my'),
    url(r'(?P<pk>[\w-]+)/finish$', finish_batch, name='finish'),
    url(r'(?P<pk>[\w-]+)/restart', restart_batch, name='restart'),
]
