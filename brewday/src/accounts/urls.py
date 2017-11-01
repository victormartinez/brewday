from django.conf.urls import url

from .views import profile, profile_password

urlpatterns = [
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/password/$', profile_password, name='profile_password'),
]
