"""flace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
1. Add an import:  from other_app.views import Home
2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
1. Import the include() function: from django.conf.urls import url, include
2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
# from django.conf.urls.static import static
from flace import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
urlpatterns = [
	url(r'^$', views.homepage),
	url(r'^about$', views.homepage, name='about'),
	url(r'^trips$', views.trips, name='trips'),
	url(r'where-are-we-now$', views.trips, name='where-are-we-now'),
	url(r'recommendations$', views.trips, name='recommendations'),
	url(r'^admin/', admin.site.urls)
]

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', views.index, name='index'),
#     url(r'^posts/$', views.get_posts),
#     url(r'^posts/(?P<pk>[0-9]+)/$', views.get_post)
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
