from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models.users import User
from ..serializers.UserSerializer import UserSerializer
from ..serializers.UserDetailSerializer import UserDetailSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        # Si consultamos un usuario por ID, usamos el detallado para ver sus préstamos
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerializer

    def get_queryset(self):
        # Optimizamos trayendo los préstamos vinculados a este usuario de un solo golpe
        if self.action == 'retrieve':
            return User.objects.prefetch_related('loan_set')
        return User.objects.all()