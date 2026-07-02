from rest_framework import serializers
from ..models.loans import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
        read_only_fields = [
            'loanDate', 
            'dueDate', 
            'loanStatus'
        ]

    def validate(self, attrs):
        book_copy = attrs.get('book_copy')
        
        if not self.instance:
            if book_copy and not book_copy.is_available:
                raise serializers.ValidationError({
                    "book_copy": "Esta copia de libro no está disponible para préstamo en este momento."
                })
            
            if attrs.get('returnDate') is not None:
                raise serializers.ValidationError({
                    "returnDate": "No puedes asignar una fecha de devolución al crear un préstamo."
                })

        else:
            if book_copy and book_copy != self.instance.book_copy and not book_copy.is_available:
                raise serializers.ValidationError({
                    "book_copy": "La nueva copia seleccionada no está disponible."
                })
                
        return attrs