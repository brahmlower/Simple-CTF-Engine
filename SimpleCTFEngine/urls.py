from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.contrib import admin
import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', views.login),
	url(r'^logout/$', views.logout),
	url(r'^home/$', views.home),
	url(r'^settings/$', views.settings),
	url(r'^manage-keys/$', views.managekeys),
	url(r'^submit-key/(?P<keyId>[0-9]+)/$', views.submitkey),
	url(r'^overview/$', views.overview),
	url(r'^$', RedirectView.as_view(url='overview/', permanent=False), name='index')
]