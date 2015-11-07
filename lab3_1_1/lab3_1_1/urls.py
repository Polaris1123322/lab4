from django.conf.urls import patterns, include, url

from django.conf.urls.defaults import *
from BookDB.views import*
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^$', books),
    (r'^books/$', books),
    (r'^admin/', include(admin.site.urls)),
    (r'^book_detail/', book_detail),
    (r'^add_book/$', add_book),
    (r'^new_book/$', new_book),
    (r'^add_author/$', add_author),
    (r'^new_author/$', new_author),
    (r'^book_delete/', book_delete),
    (r'^book_editor/', book_editor),
    ('^static/(?P<path>.*))$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)