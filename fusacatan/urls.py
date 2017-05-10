from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from material.frontend import urls as frontend_urls
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', TemplateView.as_view(template_name="home.html"),
        name="home"),
    url(r'^', include('zones.urls', namespace='zones')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
