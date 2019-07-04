from rest_framework import permissions


class IsProvince(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method and request.user.groups.filter(name='provinsi'):
            return True
        return False


class IsRegencyKelembagaan(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='kabupaten'):
            return True
        return False


class IsVillageKelembagaan(permissions.BasePermission):
    def has_objects_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.kelembagaan == request.kelembagaan


class IsDistrict(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='kecamatan'):
            return True
        return False


class IsOwnProfileOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsOwnUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.profile == request.user.profile


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile == request.user.profile
