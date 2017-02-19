# web/urls.py
from django.conf.urls import  url

from web_app.views import index

app_name = 'web' 
urlpatterns = [
	url(r'^$', index, name='index'),
]