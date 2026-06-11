from rest_framework import serializers
from .CategorySerializer import CategorySerializer
from ..models.books_categories import BookCategory

class CategoryDetailSerializer(CategorySerializer):
    libros = serializers.SerializerMethodField()

    class Meta(CategorySerializer.Meta):
        fields = '__all__'

    def get_libros(self, obj):
        # Buscamos todas las relaciones activas de esta categoría con libros
        relaciones = BookCategory.objects.filter(category=obj, status=True)
        # Retornamos los datos principales de los libros asociados
        return [
            {
                "id": rel.book.id,
                "title": rel.book.title 
            }
            for rel in relaciones
        ]