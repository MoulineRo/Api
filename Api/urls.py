
from django.urls import path, include



urlpatterns = [
    path("api/v2/", include("polls.urls")),
<<<<<<< HEAD

=======
    path("admin/", admin.site.urls),
>>>>>>> origin/second
]
