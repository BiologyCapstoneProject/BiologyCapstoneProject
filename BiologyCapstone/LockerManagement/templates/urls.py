# templates/urls.py
from django.conf.urls import  url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from web_app.views import rekt


app_name = 'templates' 
urlpatterns = [
	url(r'^$', rekt, name='rekt'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


