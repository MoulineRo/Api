import json

from django.views.decorators.csrf import csrf_exempt

from .mono import create_order

from .models import BooksModel, Order
from .serializers import ValidateFormSerializer, OrderSerializer, OrderModelSerializer
from django.http import JsonResponse, HttpResponse

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


@csrf_exempt
def webhook(request):
    if request.method == "POST":
        print(json.loads(request.body))
        Order.objects.create(
            books=json.loads(request.body)["reference"],
            total_price=json.loads(request.body)["amount"],
            created_at=json.loads(request.body)["createdDate"],
            invoice_id=json.loads(request.body)["invoiceId"],
            status=json.loads(request.body)["Email"],
        )

        return HttpResponse(request.body, status=200)
