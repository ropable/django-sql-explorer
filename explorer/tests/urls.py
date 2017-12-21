#from django.conf.urls import *
from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from explorer.urls import urlpatterns

admin.autodiscover()

urlpatterns += [
    path('admin/', admin.site.urls),
    #url(r'^admin/', include(admin.site.get_urls(), 'admin')),
]

urlpatterns += staticfiles_urlpatterns()
