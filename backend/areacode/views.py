from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from core.pagination import SmallSetPagination
from areacode.models import Province, Regency, District, Village
from areacode import serializers


class ProvinceViewSet(viewsets.ReadOnlyModelViewSet):
    """Manage tags in the database"""

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Province.objects.all()
    serializer_class = serializers.ProvinceSerializer
    pagination_class = SmallSetPagination


class RegencyViewSet(viewsets.ReadOnlyModelViewSet):
    """Manage tags in the database"""
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.RegencySerializer
    pagination_class = SmallSetPagination

    def get_queryset(self):
        queryset = Regency.objects.all()
        province = self.request.query_params.get('province')

        if province is not None:
            queryset = queryset.filter(province=province)
        return queryset


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    """Manage tags in the database"""
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.DistrictSerializer
    pagination_class = SmallSetPagination

    def get_queryset(self):
        queryset = District.objects.all()
        regency = self.request.query_params.get('regency')

        if regency is not None:
            queryset = queryset.filter(regency=regency)
        return queryset


class VillageViewSet(viewsets.ReadOnlyModelViewSet):
    """Manage tags in the database"""
    permission_classes = (AllowAny,)
    serializer_class = serializers.VillageSerializer
    pagination_class = SmallSetPagination

    def get_queryset(self):
        queryset = Village.objects.all()
        district = self.request.query_params.get('district')

        if district is not None:
            queryset = queryset.filter(district=district)
        return queryset
