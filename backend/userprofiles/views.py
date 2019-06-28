from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwnerOrReadOnly, IsOwnProfileOrReadOnly
from .serializers import (ProfileAvatarSerializer,
                                      ProfileSerializer)
from .models import Profile


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object


class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["city"]