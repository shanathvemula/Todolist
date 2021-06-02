from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("lists/", include("lists.urls")),
    path("", include("accounts.urls")),
    path("api/", include("api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
]
