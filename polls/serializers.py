
from .models import BooksModel



from rest_framework import serializers


class ValidateFormSerializer(serializers.Serializer):
    book = serializers.CharField(required=True, max_length=32)
    author = serializers.CharField(required=True, max_length=128)
    genre = serializers.CharField(required=True, max_length=128)
    date = serializers.DateField(required=True)

    class Meta:
        model = BooksModel
        fields = ["book", "author", "genre", "date"]

    def create(self, validated_data):
        return BooksModel.objects.create(**validated_data)


