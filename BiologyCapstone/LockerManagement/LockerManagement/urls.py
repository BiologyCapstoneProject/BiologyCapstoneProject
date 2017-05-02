"""
Maps the view patterns for the urls.
"""

from django.conf.urls import include,  url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from student import views

urlpatterns = [
    url(r'^$', views.RequestView, name='request'),
    url(r'^thanks/', views.SubmissionView, name='request'),
    url(r'^admin/', admin.site.urls),
    ]




