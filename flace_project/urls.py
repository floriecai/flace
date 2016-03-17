from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from flace import views

router = routers.DefaultRouter()
urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^admin/', admin.site.urls)
]