from rest_framework import serializers
from .AuthorSerializer import AuthorSerializer
from ..models.authors_books import AuthorBook

class AuthorDetailSerializer(AuthorSerializer):
    libros = serializers.SerializerMethodField()

    class Meta(AuthorSerializer.Meta):
        fields = '__all__'

    def get_libros(self, obj):
        # Buscamos todas las relaciones activas de este autor con libros
        relaciones = AuthorBook.objects.filter(author=obj, status=True)
        # Retornamos los datos clave de cada libro asociado
        return [
            {
                "id": rel.book.id, 
                "title": rel.book.title
            } 
            for rel in relaciones
        ]