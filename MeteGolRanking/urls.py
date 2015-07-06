from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'MeteGolRanking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('Public.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
