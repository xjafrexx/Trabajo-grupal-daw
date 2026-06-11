from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models.authors import Author
from ..serializers.AuthorSerializer import AuthorSerializer
from ..serializers.AuthorDetailSerializer import AuthorDetailSerializer


class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        # Si es un GET por ID (retrieve), usa el detallado. Si no, usa el plano.
        if self.action == 'retrieve':
            return AuthorDetailSerializer
        return AuthorSerializer

    def get_queryset(self):
        # Optimizamos trayendo los libros asociados a través de la tabla intermedia
        if self.action == 'retrieve':
            return Author.objects.prefetch_related('authorbook_set__book')
        return Author.objects.all()