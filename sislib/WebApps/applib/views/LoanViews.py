from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models.loans import Loan
from ..serializers.LoanSerializer import LoanSerializer
from ..serializers.LoanDetailSerializer import LoanDetailSerializer


class LoanViewSet(viewsets.ModelViewSet):

    queryset = Loan.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        # Si consultamos un préstamo en específico, usamos el detallado (anidado)
        if self.action == 'retrieve':
            return LoanDetailSerializer
        return LoanSerializer

    def get_queryset(self):
        # Usamos select_related porque 'user' y 'book_copy' son ForeignKeys directas
        if self.action == 'retrieve':
            return Loan.objects.select_related('user', 'book_copy')
        return Loan.objects.all()