from rest_framework import serializers
from .CategorySerializer import CategorySerializer
from ..models.books import Book

class CategoryBookRepresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']


class CategoryDetailSerializer(CategorySerializer):
    books = CategoryBookRepresentationSerializer(many=True, read_only=True)

    class Meta(CategorySerializer.Meta):
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