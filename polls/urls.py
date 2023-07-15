from django.urls import path, re_path, include
from django.views.decorators.csrf import csrf_exempt
from .views import Booksget, Booksid, Authors, Authorid



urlpatterns = [
    path("books/", csrf_exempt(Booksget.as_view()), name="books"),
    path("books/<int:id>/", csrf_exempt(Booksid.as_view()), name="booksid"),
    path("authors/", csrf_exempt(Authors.as_view()), name="authors"),
    path("authors/<int:id>/", csrf_exempt(Authorid.as_view()), name="authorsid"),
    path('auth/', include('djoser.urls')),
    re_path(r"^auth/", include('djoser.urls.authtoken')),



]
