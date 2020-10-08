from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from core.views import robots_txt

from search import views as search_views
from wagtail.contrib.sitemaps.views import sitemap
from .api import api_router


urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    
    url(r'^sitemap\.xml$', sitemap),
    url(r'^robots\.txt$', robots_txt, name='robots'),

    # All Auth
    # path('accounts/', include('allauth.urls')),
    url(r"", include('allauth.urls')),

    # API
    path('api/v2/', api_router.urls),

    # Wagtail URLS
    url(r"", include(wagtail_urls)),
]
