from rest_framework import serializers
from .BookSerializer import BookSerializer
from ..models.authors_books import AuthorBook
from ..models.books_categories import BookCategory
from ..models.book_copies import BookCopy

class BookDetailSerializer(BookSerializer):
    autores = serializers.SerializerMethodField()
    categorias = serializers.SerializerMethodField()
    total_copias = serializers.SerializerMethodField()
    copias_disponibles = serializers.SerializerMethodField()

    class Meta(BookSerializer.Meta):
        fields = '__all__'

    def get_autores(self, obj):
        # Buscamos las relaciones activas con autores
        relaciones = AuthorBook.objects.filter(book=obj, status=True)
        return [{"id": rel.author.id, "fullName": rel.author.fullName} for rel in relaciones]

    def get_categorias(self, obj):
        # Buscamos las relaciones activas con categorías
        relaciones = BookCategory.objects.filter(book=obj, status=True)
        return [{"id": rel.category.id, "categoryName": rel.category.categoryName} for rel in relaciones]

    def get_total_copias(self, obj):
        # Cuenta cuántas copias físicas existen de este libro en el inventario
        return BookCopy.objects.filter(book=obj, status=True).count()

    def get_copias_disponibles(self, obj):
        # Cuenta cuántas de esas copias están listas para prestarse (is_available=True)
        return BookCopy.objects.filter(book=obj, is_available=True, status=True).count()