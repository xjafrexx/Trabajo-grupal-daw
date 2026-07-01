from rest_framework import serializers
from .AuthorSerializer import AuthorSerializer
from ..models.books import Book

class AuthorBookRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']


class AuthorDetailSerializer(AuthorSerializer):
    books = AuthorBookRepresentationSerializer(many=True, read_only=True)

    class Meta(AuthorSerializer.Meta):
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['books'] = [
            {
                "id": book.id, 
                "title": book.title
            } 
            for book in instance.books.filter(status=True)
        ]
        
        return representation