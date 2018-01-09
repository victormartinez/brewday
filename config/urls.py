from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('src.core.urls', namespace='core')),
    url(r'^api/v1/ingredient-types/', include('src.ingredients.api.urls', namespace='ingredient-types-api')),
    url(r'^api/v1/equipments/', include('src.equipments.api.urls', namespace='equipments-api')),
    url(r'^accounts/', include('src.accounts.urls', namespace='accounts')),
    url(r'^recipes/', include('src.recipes.urls', namespace='recipes')),
    url(r'^ingredients/', include('src.ingredients.urls', namespace='ingredients')),
    url(r'^equipments/', include('src.equipments.urls', namespace='equipments')),
    url(r'^batches/', include('src.batches.urls', namespace='batches')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
