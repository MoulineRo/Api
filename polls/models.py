from django.db import models


class BooksModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    book = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField()


class Order(models.Model):
    books = models.ManyToManyField(BooksModel, through="OrderItem")
    total_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    invoice_id = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)


class OrderItem(models.Model):
    book = models.ForeignKey(BooksModel, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()




