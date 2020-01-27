from django.conf.urls import include, url
from django.contrib import admin
from auth_app.views import home

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'login/', include('shopify_auth.urls')),
    url(r'^$', home),
]
