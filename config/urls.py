from workbooks.models import Answer
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from django.conf import settings

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from dj_rest_auth.registration.views import VerifyEmailView
from wagtail.admin import urls as wagtailadmin_urls

from users.api.views import AccountViewSet, GroupViewSet
from workbooks.api.views import PublicWorkbookViewSet, OwnerWorkbookViewSet, PublicChapterViewSet, OwnerChapterViewSet, PublicQuestionViewSet, OwnerQuestionViewSet, OwnerAnswerViewSet
from orders.api.views import OrderViewSet, OrderItemViewSet
from coaches.api.views import CoachViewSet
from media.api.views import OwnerEmbedViewSet, OwnerImageViewSet
from libraries.api.views import LibraryViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'accounts', AccountViewSet, basename="accounts")
router.register(r'groups', GroupViewSet, basename="groups")
router.register(r'public/workbooks', PublicWorkbookViewSet, basename="public-workbooks")
router.register(r'public/chapters', PublicChapterViewSet, basename="public-chapters")
router.register(r'public/questions', PublicQuestionViewSet, basename="public-questions")
router.register(r'workbooks', OwnerWorkbookViewSet, basename="workbooks")
router.register(r'chapters', OwnerChapterViewSet, basename="chapters")
router.register(r'questions', OwnerQuestionViewSet, basename="questions")
router.register(r'answers', OwnerAnswerViewSet, basename="answers")
router.register(r'orders', OrderViewSet, basename="orders")
router.register(r'order-items', OrderItemViewSet, basename="order-items")
router.register(r'coaches', CoachViewSet, basename="coaches")
router.register(r'images', OwnerImageViewSet, basename="images")
router.register(r'embeds', OwnerEmbedViewSet, basename="embeds")
router.register(r'libraries', LibraryViewSet, basename="libraries")

urlpatterns = [
    path("workbook-factory/admin/docs/", include("django.contrib.admindocs.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
    path("workbook-factory/cms/", include(wagtailadmin_urls))
]


urlpatterns += [

    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),

    path('api/auth/', include('rest_framework.urls')),
    
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/', include(router.urls)),
    
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
