from rest_framework import serializers
from .UserSerializer import UserSerializer
from ..models.loans import Loan

class UserDetailSerializer(UserSerializer):
    prestamos_activos = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = '__all__'

    def get_prestamos_activos(self, obj):
        # Buscamos todos los préstamos de este usuario con estatus 'ACTIVO'
        prestamos = Loan.objects.filter(user=obj, loanStatus='ACTIVO', status=True)
        # Retornamos los datos clave de cada préstamo
        return [
            {
                "id": p.id,
                "loanDate": p.loanDate,
                "dueDate": p.dueDate,
                "barcode_copia": p.book_copy.barcode
            }
            for p in prestamos
        ]