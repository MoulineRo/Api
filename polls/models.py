from django.db import models


class BooksModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    book = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    date = models.DateField()
