import io
import time

from django.core.cache import cache
from django.http import JsonResponse
from django.views import View
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import BooksModel
from .serializers import ValidateFormSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie


class Booksget(APIView):
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def get(self, request):
        time.sleep(5)
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
        cache.clear()
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


class Booksid(View):
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def get(self, request, id):
        time.sleep(5)
        x = BooksModel.objects.values("id")
        y = {"id": id}
        if y in x:
            check = BooksModel.objects.filter(id=id).values()
            return JsonResponse(list(check)[0], safe=False, status=200)
        else:
            return JsonResponse({"error": "not found"}, safe=False, status=404)

    def put(self, request, id):
        cache.clear()
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
        cache.clear()
        x = BooksModel.objects.values("id")
        y = {"id": id}
        if y in x:
            BooksModel.objects.filter(id=id).delete()
            ret = BooksModel.objects.all().values()
            return JsonResponse(list(ret), safe=False, status=200)
        else:
            return JsonResponse({"error": "not found"}, safe=False, status=404)


class Authors(View):
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def get(self, request):
        time.sleep(5)
        author = request.GET.get("author")
        if author is not None:
            author = request.GET.get("author")
            check = BooksModel.objects.filter(author=author).values()
            return JsonResponse(list(check), safe=False, status=200)
        else:
            check = BooksModel.objects.values("author")
            return JsonResponse(list(check), safe=False, status=200)


class Authorid(View):
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def get(self, request, id):
        time.sleep(5)
        x = BooksModel.objects.values("id")
        y = {"id": id}
        if y in x:
            check = BooksModel.objects.filter(id=id).values()
            return JsonResponse(list(check)[0], safe=False, status=200)
        else:
            return JsonResponse({"error": "not found"}, safe=False, status=404)
