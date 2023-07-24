from .models import BooksModel, Order


from rest_framework import serializers


class ValidateFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = ["id", "book", "author", "quantity", "price"]


class OrderContentSerializer(serializers.Serializer):
    book_id = serializers.PrimaryKeyRelatedField(queryset=BooksModel.objects.all())
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.Serializer):
    order = OrderContentSerializer(many=True, allow_empty=False)


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["total_price", "created_at", "invoice_id", "id", "books", "status"]


class MonoCallbackSerializer(serializers.Serializer):
    invoiceId = serializers.CharField()
    status = serializers.CharField()
    amount = serializers.IntegerField()
    ccy = serializers.IntegerField()
    reference = serializers.CharField()
