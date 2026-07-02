from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.db import transaction

from ..models.loans import Loan
from ..serializers.LoanSerializer import LoanSerializer
from ..serializers.LoanDetailSerializer import LoanDetailSerializer


class LoanViewSet(viewsets.ModelViewSet):

    queryset = Loan.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return LoanDetailSerializer
        return LoanSerializer

    def get_queryset(self):
        if self.action == 'retrieve':
            return Loan.objects.select_related('user', 'book_copy')
        return Loan.objects.all()

    @transaction.atomic
    def perform_create(self, serializer):
        loan = serializer.save()

        book_copy = loan.book_copy
        book_copy.is_available = False
        book_copy.save(update_fields=['is_available'])

    @transaction.atomic
    def perform_update(self, serializer):
        instance = self.get_object()
        loan = serializer.save()

        if instance.returnDate is None and loan.returnDate is not None:
            loan.book_copy.is_available = True
            loan.book_copy.save(update_fields=['is_available'])

            loan.loanStatus = 'Devuelto'
            loan.save(update_fields=['loanStatus'])