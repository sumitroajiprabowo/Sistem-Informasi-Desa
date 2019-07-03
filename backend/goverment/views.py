from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        )
from .serializers import KelembagaanSerializers, JabatanSerializers
from .models import Kelembagaan, Jabatan


class KelembagaanView(viewsets.ModelViewSet):
    """Create kelembagaan in the system"""
    queryset = Kelembagaan.objects.all()
    serializer_class = KelembagaanSerializers
    permission_classes = (IsAuthenticated,)


class JabatanView(viewsets.ModelViewSet):
    """Create Jabatan in the system"""
    queryset = Jabatan.objects.all()
    serializer_class = JabatanSerializers
    permission_classes = (IsAuthenticated,)
