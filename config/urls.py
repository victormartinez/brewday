from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('src.core.urls', namespace='core')),
    url(r'^accounts/', include('src.accounts.urls', namespace='accounts')),
    url(r'^recipes/', include('src.recipes.urls', namespace='recipes')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
