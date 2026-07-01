from rest_framework import serializers
from ..models.book_copies import BookCopy

class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = '__all__'