from django.urls import path, include
from .views import BookViewsSet, OrderView, OrderViewsSet, OrderCallBackView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"books", BookViewsSet)
router.register(r"orders", OrderViewsSet)

urlpatterns = [
    path("", include(router.urls)),
    path("order/", OrderView.as_view()),
    path("callback/", OrderCallBackView.as_view()),
]
