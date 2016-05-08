from django.conf.urls import patterns, include, url
from django.contrib import admin
#from newsite.views import menu
from restaurants.views import menu

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^menu/$', menu),
)
