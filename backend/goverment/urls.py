from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import KelembagaanView, JabatanView

router = DefaultRouter()
router.register(r"kelembagaan", KelembagaanView, base_name='kelembagaan')
router.register(r"jabatan", JabatanView, base_name='jabatan')


urlpatterns = [
    path("", include(router.urls)),
]
