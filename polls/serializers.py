from .models import BooksModel, Order


from rest_framework import serializers


class ValidateFormSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    book = serializers.CharField(required=True, max_length=32)
    author = serializers.CharField(required=True, max_length=128)
    quantity = serializers.IntegerField(required=True, max_value=1000)
    price = serializers.IntegerField(required=True, max_value=1000)

    class Meta:
        model = BooksModel
        fields = ["id", "book", "author", "quantity", "price"]

    def create(self, validated_data):
        return BooksModel.objects.create(**validated_data)


class OrderContentSerializer(serializers.Serializer):
    book_id = serializers.PrimaryKeyRelatedField(queryset=BooksModel.objects.all())
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.Serializer):
    order = OrderContentSerializer(many=True, allow_empty=False)


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["total_price", "created_at", "invoice_id", "id", "books", "status"]
