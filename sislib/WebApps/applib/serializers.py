from rest_framework import serializers
from .models.books import Book
from .models.authors import Author
from .models.categories import Category
from .models.authors_books import AuthorBook
from .models.books_categories import BookCategory

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    autores = serializers.SerializerMethodField()
    categorias = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_autores(self, obj):
        relaciones = AuthorBook.objects.filter(book=obj, status=True)
        return [{"id": rel.author.id, "fullName": rel.author.fullName} for rel in relaciones]

    def get_categorias(self, obj):
        relaciones = BookCategory.objects.filter(book=obj, status=True)
        return [{"id": rel.category.id, "categoryName": rel.category.categoryName} for rel in relaciones]