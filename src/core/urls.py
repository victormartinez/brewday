from django.conf.urls import url

from ..accounts.views import login, logout, register, forgot_password, reset_password
from .views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
    url(r'^register$', register, name='register'),
    url(r'^forgot-password$', forgot_password, name='forgot_password'),
    url(r'^reset-password/(?P<uidb64>\w+)/(?P<token>[\w-]+)$', reset_password, name='reset_password'),
]
