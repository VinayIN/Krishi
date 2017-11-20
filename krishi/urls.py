
from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^farmer/',include('farmer.urls')),
    url(r'^market/',include('market.urls')),
    url(r'^crop_warehouse/',include('crop_warehouse.urls')),
    url(r'^transport/',include('transport.urls')),
]
