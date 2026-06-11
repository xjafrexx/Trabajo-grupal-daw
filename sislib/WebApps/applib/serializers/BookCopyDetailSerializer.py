from rest_framework import serializers
from .BookCopySerializer import BookCopySerializer
from .BookSerializer import BookSerializer

class BookCopyDetailSerializer(BookCopySerializer):
    # Anidamos el serializador de libros para ver toda su información al leer la copia
    book = BookSerializer(read_only=True)

    class Meta(BookCopySerializer.Meta):
        fields = '__all__'