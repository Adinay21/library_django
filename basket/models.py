from django.db import models
from categories_of_books.models import Book


class BasketModel(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120, null=True)
    phone_number = models.CharField(max_length=120)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='baskets', null=True)

    def __str__(self):
        return self.name

