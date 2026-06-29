from rest_framework import serializers
from django.db import transaction
from ..models.books import Book
from ..models.authors import Author
from ..models.categories import Category
from ..models.authors_books import AuthorBook
from ..models.books_categories import BookCategory

class BookAuthorReadSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    fullName = serializers.CharField()

class BookCategoryReadSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    categoryName = serializers.CharField()

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Author.objects.filter(status=True),
        required=False
    )
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.filter(status=True),
        required=False
    )

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('created', 'modified', 'created_id', 'modified_id')

    def create(self, validated_data):
        authors_data = validated_data.pop('authors', [])
        categories_data = validated_data.pop('categories', [])
        
        request = self.context.get('request')
        user = request.user if request and request.user.is_authenticated else None

        with transaction.atomic():
            book = Book.objects.create(created_id=user, modified_id=user, **validated_data)
            
            author_links = [
                AuthorBook(book=book, author=author, created_id=user, modified_id=user)
                for author in authors_data
            ]
            AuthorBook.objects.bulk_create(author_links)
            
            category_links = [
                BookCategory(book=book, category=category, created_id=user, modified_id=user)
                for category in categories_data
            ]
            BookCategory.objects.bulk_create(category_links)
                
        return book

    def update(self, instance, validated_data):
        authors_data = validated_data.pop('authors', None)
        categories_data = validated_data.pop('categories', None)
        
        request = self.context.get('request')
        user = request.user if request and request.user.is_authenticated else None

        with transaction.atomic():
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.modified_id = user
            instance.save()

            if authors_data is not None:
                new_author_ids = [author.id for author in authors_data]
                AuthorBook.objects.filter(book=instance).exclude(author_id__in=new_author_ids).delete()
                for author in authors_data:
                    AuthorBook.objects.get_or_create(
                        book=instance, author=author,
                        defaults={'created_id': user, 'modified_id': user}
                    )

            if categories_data is not None:
                new_category_ids = [category.id for category in categories_data]
                BookCategory.objects.filter(book=instance).exclude(category_id__in=new_category_ids).delete()
                for category in categories_data:
                    BookCategory.objects.get_or_create(
                        book=instance, category=category,
                        defaults={'created_id': user, 'modified_id': user}
                    )
                    
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation['authors'] = [
            {'id': author.id, 'fullName': author.fullName} 
            for author in instance.authors.filter(status=True)
        ]
        
        representation['categories'] = [
            {'id': category.id, 'categoryName': category.categoryName} 
            for category in instance.categories.filter(status=True)
        ]
        
        return representation