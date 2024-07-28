from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Configuration drf-yasg
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Configuration drf-yasg
schema_view = get_schema_view(
   openapi.Info(
      title="Blog Passion API",
      default_version='v1',
      description="An API to manage Blog Passion",
      contact=openapi.Contact(email="contact@blog-passion.fr"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

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
    # Configuration drf-yasg
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), 
        name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), 
        name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), 
        name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )