from rest_framework import serializers
from .LoanSerializer import LoanSerializer
from .UserSerializer import UserSerializer
from .BookCopyDetailSerializer import BookCopyDetailSerializer

class LoanDetailSerializer(LoanSerializer):
    # Anidamos los serializadores para expandir la información en las consultas GET
    user = UserSerializer(read_only=True)
    book_copy = BookCopyDetailSerializer(read_only=True)

    class Meta(LoanSerializer.Meta):
        fields = '__all__'