from workbooks.models import Answer
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from django.conf import settings

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from users.api.views import AccountViewSet, GroupViewSet
from workbooks.api.views import WorkbookViewSet, ChapterViewSet, PageViewSet, QuestionViewSet, AnswerViewSet
from orders.api.views import OrderViewSet, OrderItemViewSet
from coaches.api.views import CoachViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'accounts', AccountViewSet, basename="accounts")
router.register(r'groups', GroupViewSet, basename="groups")
router.register(r'workbooks', WorkbookViewSet, basename="workbooks")
router.register(r'chapters', ChapterViewSet, basename="chapters")
router.register(r'pages', PageViewSet, basename="pages")
router.register(r'questions', QuestionViewSet, basename="questions")
router.register(r'answers', AnswerViewSet, basename="answers")
router.register(r'orders', OrderViewSet, basename="orders")
router.register(r'order-items', OrderItemViewSet, basename="order-items")
router.register(r'coaches', CoachViewSet, basename="coaches")

urlpatterns = [
    path("workbook-factory/admin/docs/", include("django.contrib.admindocs.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]


urlpatterns += [
    path('api/auth/', include('rest_framework.urls')),
    
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),

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
