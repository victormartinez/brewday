from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('src.core.urls', namespace='core')),
    url(r'^accounts/', include('src.accounts.urls', namespace='accounts')),
    url(r'^recipes/', include('src.recipes.urls', namespace='recipes')),
    url(r'^ingredients/', include('src.ingredients.urls', namespace='ingredients')),
    url(r'^equipments/', include('src.equipments.urls', namespace='equipments')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
