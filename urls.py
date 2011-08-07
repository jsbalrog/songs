from django.conf.urls.defaults import patterns, include, url
from songster import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^list/$', views.list),
	url(r'^search/$', views.search),
    # url(r'^$', 'songs.views.home', name='home'),
    # url(r'^songs/', include('songs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
