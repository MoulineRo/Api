from .mono import create_order

from .models import BooksModel, Order
from .serializers import ValidateFormSerializer, OrderSerializer, OrderModelSerializer
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions


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
        order_data = create_order(order.validated_data["order"])
        return JsonResponse(order_data)


class OrderCallBackView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        return JsonResponse({"status": "ok"})
