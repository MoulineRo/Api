import json

from django.http import JsonResponse
from django.views import View
from .models import BooksModel


class Booksget(View):
    def get(self, request):
        book = request.GET.get("book")
        author = request.GET.get("author")
        genre = request.GET.get("genre")
        if book is not None:
            check = BooksModel.objects.filter(book=book).values()
            return JsonResponse(list(check),safe=False, status=200)
        if author is not None:
            check = BooksModel.objects.filter(author=author).values()
            return JsonResponse(list(check),safe=False, status=200)
        if genre is not None:
            check = BooksModel.objects.filter(genre=genre).values()
            return JsonResponse(list(check),safe=False, status=200)
        else:
            check = BooksModel.objects.all().values()
            return JsonResponse(list(check),safe=False, status=200)

    def post(self, request):
        try:
            request_body = json.loads(request.body)
        except ValueError:
            return JsonResponse({"error": "invalid json"},safe=False, status=400)

        if not request_body["book"]:
            return JsonResponse({"error": "missing name field"},safe=False, status=400)
        if not request_body["author"]:
            return JsonResponse({"error": "missing name field"},safe=False, status=400)
        if not request_body["genre"]:
            return JsonResponse({"error": "missing name field"},safe=False, status=400)

        BooksModel.objects.create(
            id=request_body["id"],
            book=request_body["book"],
            author=request_body["author"],
            genre=request_body["genre"],
            date=request_body["date"],
        )
        ret = BooksModel.objects.all().values()
        return JsonResponse(list(ret),safe=False, status=200)


class Booksid(View):
    def get(self, request, id):
        check = BooksModel.objects.filter(id=id).values()
        return JsonResponse(list(check),safe=False, status=200)

    def put(self, request, id):
        try:
            request_body = json.loads(request.body)
        except ValueError:
            return JsonResponse({"error": "invalid json"},safe=False, status=400)

        if not request_body["book"]:
            return JsonResponse({"error": "this params not found"},safe=False, status=404)
        if not request_body["author"]:
            return JsonResponse({"error": "this params not found"},safe=False, status=404)
        if not request_body["genre"]:
            return JsonResponse({"error": "this params not found"},safe=False, status=404)

        BooksModel.objects.filter(id=id).update(
            book=request_body["book"],
            author=request_body["author"],
            genre=request_body["genre"],
            date=request_body["date"],
        )
        ret = BooksModel.objects.all().values()
        return JsonResponse(list(ret),safe=False, status=200)

    def delete(self, request, id):
        BooksModel.objects.filter(id=id).delete()
        ret = BooksModel.objects.all().values()
        return JsonResponse(list(ret),safe=False, status=200)


class Authors(View):
    def get(self, request):
        author = request.GET.get("author")
        if author is not None:
            author = request.GET.get("author")
            check = BooksModel.objects.filter(author=author).values()
            return JsonResponse(list(check),safe=False, status=200)
        else:
            check = BooksModel.objects.values("author")
            return JsonResponse(list(check),safe=False, status=200)


class Authorid(View):
    def get(self, request, id):
        check = BooksModel.objects.filter(id=id).values()
        return JsonResponse(list(check),safe=False, status=200)
