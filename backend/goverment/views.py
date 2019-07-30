from rest_framework import (generics, mixins, viewsets,
                            authentication)

from rest_framework.permissions import (IsAuthenticated,
                                        )
from .serializers import (KelembagaanSerializers, JabatanSerializers,
                          PemerintahanSerializers, VillageGovermentSerializers,
                          VillageGovermentDetailSerializers)
from .models import Kelembagaan, Jabatan, Pemerintahan
from .permissions import (IsRegencyKelembagaan,
                          IsOwnVillageGovermentsOrReadOnly,
                          IsVillages)


class KelembagaanViewsetRegency(viewsets.ModelViewSet):
    """Create kelembagaan in the system"""
    serializer_class = KelembagaanSerializers
    permission_classes = [IsAuthenticated, IsRegencyKelembagaan]
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        queryset = Kelembagaan.objects.all()
        return queryset


class KelembagaanReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    """Create kelembagaan in the system"""
    serializer_class = KelembagaanSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        queryset = Kelembagaan.objects.all()
        return queryset


class JabatanViewSetRegency(viewsets.ModelViewSet):
    """Create Jabatan in the system"""
    serializer_class = JabatanSerializers
    permission_classes = (IsAuthenticated, IsRegencyKelembagaan)
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        queryset = Jabatan.objects.all()
        kelembagaan = self.request.query_params.get('kelembagaan')

        if kelembagaan is not None:
            queryset = queryset.filter(kelembagaan=kelembagaan)
        return queryset


class JabatanReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
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


class CreateVillageGovermentView(generics.CreateAPIView):
    """Create village goverment"""
    serializer_class = PemerintahanSerializers


class VillageGovermentTestsViewSet(viewsets.ModelViewSet):
    serializer_class = PemerintahanSerializers
    queryset = Pemerintahan.objects.all()
    permission_classes = (IsAuthenticated, IsOwnVillageGovermentsOrReadOnly,
                          IsVillages, )
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        queryset = Pemerintahan.objects.all()
        # return self.queryset.filter(user=self.request.user)
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class VillageGovermentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VillageGovermentSerializers
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwnVillageGovermentsOrReadOnly,
                          IsVillages, )

    def get_queryset(self):
        """Retrieve and return authentication user"""
        return Pemerintahan.objects.filter(user=self.request.user)


class VillageGovermentDetailViewSet(mixins.UpdateModelMixin,
                                    mixins.ListModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet):
    queryset = Pemerintahan.objects.all()
    serializer_class = VillageGovermentDetailSerializers
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsVillages, )

    def get_queryset(self):
        """Retrieve villages goverment data user"""
        return Pemerintahan.objects.filter(user=self.request.user)
