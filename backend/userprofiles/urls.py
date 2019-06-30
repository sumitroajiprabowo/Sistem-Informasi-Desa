from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (CreateUserView, CreateTokenView,
                    AvatarUpdateView, ProfileViewSet,
                    ProfileStatusViewSet, UserProfileViewSet)

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"lihat", UserProfileViewSet)
router.register(r"status", ProfileStatusViewSet, basename="status")


urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update"),
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', CreateTokenView.as_view(), name='login'),
]
