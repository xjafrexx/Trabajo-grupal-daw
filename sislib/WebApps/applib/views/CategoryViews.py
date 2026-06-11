from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models.categories import Category
from ..serializers.CategorySerializer import CategorySerializer
from ..serializers.CategoryDetailSerializer import CategoryDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        # Si consultamos una categoría en particular, usamos el detallado
        if self.action == 'retrieve':
            return CategoryDetailSerializer
        return CategorySerializer

    def get_queryset(self):
        # Optimizamos trayendo los libros asociados mediante la tabla intermedia
        if self.action == 'retrieve':
            return Category.objects.prefetch_related('bookcategory_set__book')
        return Category.objects.all()