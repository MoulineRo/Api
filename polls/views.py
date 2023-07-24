import requests

from django.urls import reverse

from Api import settings
from .mono import create_order, verify_signature

from .models import BooksModel, Order
from .serializers import (
    ValidateFormSerializer,
    OrderSerializer,
    OrderModelSerializer,
    MonoCallbackSerializer,
)
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response


class BookViewsSet(viewsets.ModelViewSet):
    queryset = BooksModel.objects.all().order_by("id")
    serializer_class = ValidateFormSerializer
    permission_classes = [permissions.AllowAny]


class OrderViewsSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all().order_by("id")
    serializer_class = OrderModelSerializer
    permission_classes = [permissions.AllowAny]


class OrderView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        order = OrderSerializer(data=request.data)
        order.is_valid(raise_exception=True)
        webhook_url = request.build_absolute_uri(reverse("mono_callback"))
        order_data = create_order(order.validated_data["order"], webhook_url)
        return JsonResponse(order_data)


class CallBackView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        public_key = requests.get(
            "https://api.monobank.ua/api/merchant/pubkey",
            headers={"X-Token": settings.MONOBANK_API_KEY},
        ).json()["key"]
        if not verify_signature(
            public_key, request.headers.get("X-Sign"), request.body
        ):
            return Response({"status": "signature mismatch"}, status=400)

        callback = MonoCallbackSerializer(data=request.data)
        callback.is_valid(raise_exception=True)
        try:
            order = Order.objects.get(id=callback.validated_data["reference"])
        except Order.DoesNotExist:
            return Response({"status": "order not found"}, status=404)
        if order.invoice_id != callback.validated_data["invoiceId"]:
            return Response({"status": "invoiceId mismatch"}, status=400)
        order.status = callback.validated_data["status"]
        order.save()
        return Response({"status": "ok"})
