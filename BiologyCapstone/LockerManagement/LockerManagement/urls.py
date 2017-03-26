from django.conf.urls import include,  url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
#from web_app.views import rekt
from student import views
#urlpatterns = [
	#url(r'^$', templates.url, name='rekt'),
#]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    url(r'^$', views.RequestView, name='request'),
    url(r'^admin/', admin.site.urls),
    
   
   # url(r'^student', include("student.urls", namespace='index')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]




