from django.conf.urls import url

from ..accounts.views import login, logout
from .views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout')
]
