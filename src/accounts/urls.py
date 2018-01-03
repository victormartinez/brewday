from django.conf.urls import url

from .views import profile, profile_email, profile_password, profile_preferences

urlpatterns = [
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/password/$', profile_password, name='profile_password'),
    url(r'^profile/email/$', profile_email, name='profile_email'),
    url(r'^profile/preferences/$', profile_preferences, name='profile_preferences'),
]
