from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models.categories import Category
from ..serializers.CategorySerializer import CategorySerializer
from ..serializers.CategoryDetailSerializer import CategoryDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoryDetailSerializer
        return CategorySerializer

    def get_queryset(self):
        """
        Optimizamos la consulta del detalle cargando de un solo golpe 
        todos los libros asociados mediante el related_name del ManyToMany.
        """
        if self.action == 'retrieve':
            return Category.objects.prefetch_related('books')
        return Category.objects.all()