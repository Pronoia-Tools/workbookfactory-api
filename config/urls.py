from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from django.conf import settings

from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("workbook-factory/admin/docs/", include("django.contrib.admindocs.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]


urlpatterns += [
    
    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path("", TemplateView.as_view(template_name="base.html")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
