from rest_framework import viewsets, authentication
from rest_framework.permissions import (IsAuthenticated,
                                        )
from .serializers import KelembagaanSerializers, JabatanSerializers
from .models import Kelembagaan, Jabatan
from .permissions import IsRegencyKelembagaan


class KelembagaanView(viewsets.ModelViewSet):
    """Create kelembagaan in the system"""
    serializer_class = KelembagaanSerializers
    permission_classes = [IsAuthenticated, IsRegencyKelembagaan]
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        queryset = Kelembagaan.objects.all()
        return queryset

    def perform_create(self, serializer):
        user_kelembagaan = self.request.user
        serializer.save(user_kelembagaan=user_kelembagaan)


class JabatanView(viewsets.ModelViewSet):
    """Create Jabatan in the system"""
    serializer_class = JabatanSerializers
    permission_classes = (IsAuthenticated, )
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        queryset = Jabatan.objects.all()
        kelembagaan = self.request.query_params.get('kelembagaan')

        if kelembagaan is not None:
            queryset = queryset.filter(kelembagaan=kelembagaan)
        return queryset
