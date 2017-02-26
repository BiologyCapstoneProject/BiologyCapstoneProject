# templates/urls.py
from django.conf.urls import  url

from web_app.views import rekt

app_name = 'templates' 
urlpatterns = [
	url(r'^$', rekt, name='rekt'),
]