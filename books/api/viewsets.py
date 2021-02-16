from rest_framework import viewsets
from books.api import serializers
from books.models import Book

from books.api.serializers import BookSerializer


class BooksViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

