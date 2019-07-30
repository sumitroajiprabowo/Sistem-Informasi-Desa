from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (KelembagaanViewsetRegency, KelembagaanReadOnlyViewset,
                    JabatanViewSetRegency, JabatanReadOnlyViewSet,
                    CreateVillageGovermentView, VillageGovermentTestsViewSet,
                    VillageGovermentViewSet)

router = DefaultRouter()
router.register('kelembagaan/list', KelembagaanReadOnlyViewset,
                base_name='kelembagaan-list')
router.register("kelembagaan", KelembagaanViewsetRegency,
                base_name='kelembagaan')
router.register("jabatan/list", JabatanReadOnlyViewSet,
                base_name='jabatan-list')
router.register(r"jabatan", JabatanViewSetRegency,
                base_name='jabatan')
router.register("testbos", VillageGovermentTestsViewSet,
                base_name='pemdes')
router.register(r"village", VillageGovermentViewSet,
                base_name='village')


urlpatterns = [
    path("", include(router.urls)),
    path('village/create/', CreateVillageGovermentView.as_view(),
         name='create-goverment-village'),
]
