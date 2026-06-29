from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models.authors import Author
from ..serializers.AuthorSerializer import AuthorSerializer
from ..serializers.AuthorDetailSerializer import AuthorDetailSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AuthorDetailSerializer
        return AuthorSerializer

    def get_queryset(self):
        if self.action == 'retrieve':
            return Author.objects.prefetch_related('books')
        return Author.objects.all()