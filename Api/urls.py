from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/v2/", include("polls.urls")),
    path("admin/", admin.site.urls),

]
if settings.TEST:
    urlpatterns += path('',
        path(r'', include('django.contrib.staticfiles.urls')),
        )