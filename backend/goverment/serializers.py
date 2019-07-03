from rest_framework import serializers
from .models import Kelembagaan, Jabatan


class KelembagaanSerializers(serializers.ModelSerializer):

    class Meta:
        model = Kelembagaan
        fields = "__all__"


class JabatanSerializers(serializers.ModelSerializer):

    class Meta:
        model = Jabatan
        fields = "__all__"
