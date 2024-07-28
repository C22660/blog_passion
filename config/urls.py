from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.articles.urls")),
    path("events/", include("blog.events.urls")),
    path("users/", include("blog.users.urls")),
    path("contacts/", include("blog.contacts.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include("api.articles.urls")),
    path("", include('api.users.urls')),
    path("", include("api.events.urls")),
    path("", include("api.contacts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )