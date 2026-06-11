from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models.book_copies import BookCopy
from ..serializers.BookCopySerializer import BookCopySerializer
from ..serializers.BookCopyDetailSerializer import BookCopyDetailSerializer


class BookCopyViewSet(viewsets.ModelViewSet):

    queryset = BookCopy.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        # Si se consulta una copia específica por ID, usamos el detallado (anidado)
        if self.action == 'retrieve':
            return BookCopyDetailSerializer
        return BookCopySerializer

    def get_queryset(self):
        # Usamos select_related porque 'book' es una ForeignKey directa (relación 1 a muchos)
        if self.action == 'retrieve':
            return BookCopy.objects.select_related('book')
        return BookCopy.objects.all()