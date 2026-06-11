from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models.books import Book
from ..serializers.BookSerializer import BookSerializer
from ..serializers.BookDetailSerializer import BookDetailSerializer


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        # Si es un GET por ID, usamos el detallado que calcula las copias
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookSerializer

    def get_queryset(self):
        # Optimizamos las consultas de las tablas intermedias y las copias
        if self.action == 'retrieve':
            return Book.objects.prefetch_related(
                'authorbook_set__author',
                'bookcategory_set__category',
                'bookcopy_set'
            )
        return Book.objects.all()