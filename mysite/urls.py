from django.conf.urls import patterns, include, url
from django.contrib import admin
import blog.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]




# admin.autodiscover()

# urlpatterns = patterns('', url(r'^$',blog.views), url(r'^blog/', include('blog.urls')),)

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^posts/',displaypost),
# )
