from rest_framework import serializers
from .BookSerializer import BookSerializer
from ..models.book_copies import BookCopy

class BookDetailSerializer(BookSerializer):
    total_copies = serializers.SerializerMethodField()
    available_copies = serializers.SerializerMethodField()

    class Meta(BookSerializer.Meta):
        fields = '__all__'

    def get_total_copies(self, obj):
        if hasattr(obj, '_prefetched_objects_cache') and 'bookcopy_set' in obj._prefetched_objects_cache:
            return sum(1 for copia in obj.bookcopy_set.all() if copia.status)
        return BookCopy.objects.filter(book=obj, status=True).count()

    def get_available_copies(self, obj):
        if hasattr(obj, '_prefetched_objects_cache') and 'bookcopy_set' in obj._prefetched_objects_cache:
            return sum(1 for copia in obj.bookcopy_set.all() if copia.is_available and copia.status)
        return BookCopy.objects.filter(book=obj, is_available=True, status=True).count()