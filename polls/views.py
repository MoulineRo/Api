import io

from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from .models import BooksModel
from .serializers import ValidateFormSerializer
from django.http import JsonResponse

from rest_framework.views import APIView



class Booksget(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        book = request.GET.get("book")
        author = request.GET.get("author")
        genre = request.GET.get("genre")
        if book is not None:
            check = BooksModel.objects.filter(book=book).values()
            return JsonResponse(list(check), safe=False, status=200)
        if author is not None:
            check = BooksModel.objects.filter(author=author).values()
            return JsonResponse(list(check), safe=False, status=200)
        if genre is not None:
            check = BooksModel.objects.filter(genre=genre).values()
            return JsonResponse(list(check), safe=False, status=200)
        else:
            check = BooksModel.objects.all().values()
            return JsonResponse(list(check), safe=False, status=200)


    def post(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ValidateFormSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            ret = BooksModel.objects.all().values()
            return JsonResponse(list(ret), safe=False, status=200)
        else:
            return JsonResponse({"error": "missing name field"}, safe=False, status=400)


class Booksid(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        x = BooksModel.objects.values("id")
        y = {"id": id}
        if y in x:
            check = BooksModel.objects.filter(id=id).values()
            return JsonResponse(list(check)[0], safe=False, status=200)
        else:
            return JsonResponse({"error": "not found"}, safe=False, status=404)

    def put(self, request, id):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ValidateFormSerializer(data=pythondata)
        if serializer.is_valid():
            BooksModel.objects.filter(id=id).update(
                book=serializer["book"].value,
                author=serializer["author"].value,
                genre=serializer["genre"].value,
                date=serializer["date"].value,
            )
            ret = BooksModel.objects.filter(id=id).values()
            return JsonResponse(list(ret)[0], safe=False, status=200)

        return JsonResponse({"error": "missing name field"}, safe=False, status=400)

    def delete(self, request, id):
        x = BooksModel.objects.values("id")
        y = {"id": id}
        if y in x:
            BooksModel.objects.filter(id=id).delete()
            ret = BooksModel.objects.all().values()
            return JsonResponse(list(ret), safe=False, status=200)
        else:
            return JsonResponse({"error": "not found"}, safe=False, status=404)


class Authors(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        author = request.GET.get("author")
        if author is not None:
            author = request.GET.get("author")
            check = BooksModel.objects.filter(author=author).values()
            return JsonResponse(list(check), safe=False, status=200)
        else:
            check = BooksModel.objects.values("author")
            return JsonResponse(list(check), safe=False, status=200)


class Authorid(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        x = BooksModel.objects.values("id")
        y = {"id": id}
        if y in x:
            check = BooksModel.objects.filter(id=id).values()
            return JsonResponse(list(check)[0], safe=False, status=200)
        else:
            return JsonResponse({"error": "not found"}, safe=False, status=404)
