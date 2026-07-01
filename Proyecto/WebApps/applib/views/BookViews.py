from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers

from ..models.books import Book
from ..serializers.BookSerializer import BookSerializer
from ..serializers.BookDetailSerializer import BookDetailSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookSerializer

    def get_queryset(self):
        if self.action == 'retrieve':
            return Book.objects.prefetch_related(
                'authors',       
                'categories',    
                'bookcopy_set'   
            )
        
        if self.action == 'list':
            return Book.objects.prefetch_related('authors', 'categories')

        return Book.objects.all()
    
    @extend_schema(
        responses={
            200: inline_serializer(
                name='BookListResponse',
                fields={
                    **{field.name: serializers.ReadOnlyField() for field in Book._meta.fields},
                    'authors': inline_serializer(
                        name='BookAuthorResponse',
                        fields={
                            'id': serializers.UUIDField(),
                            'fullName': serializers.CharField()
                        },
                        many=True
                    ),
                    'categories': inline_serializer(
                        name='BookCategoryResponse',
                        fields={
                            'id': serializers.UUIDField(),
                            'categoryName': serializers.CharField()
                        },
                        many=True
                    )
                }
            )
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        responses={
            200: inline_serializer(
                name='BookDetailResponse',
                fields={
                    **{field.name: serializers.ReadOnlyField() for field in Book._meta.fields},
                    'authors': inline_serializer(
                        name='BookAuthorDetailResponse',
                        fields={
                            'id': serializers.UUIDField(),
                            'fullName': serializers.CharField()
                        },
                        many=True
                    ),
                    'categories': inline_serializer(
                        name='BookCategoryDetailResponse',
                        fields={
                            'id': serializers.UUIDField(),
                            'categoryName': serializers.CharField()
                        },
                        many=True
                    ),
                    'total_copies': serializers.IntegerField(),
                    'available_copies': serializers.IntegerField()
                }
            )
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)