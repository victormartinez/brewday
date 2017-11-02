from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('src.core.urls', namespace='core')),
    url(r'^accounts/', include('src.accounts.urls', namespace='accounts')),
]