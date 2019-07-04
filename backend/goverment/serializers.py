from rest_framework import serializers
from .models import Kelembagaan, Jabatan


class KelembagaanSerializers(serializers.ModelSerializer):
    user_kelembagaan = serializers.StringRelatedField(
        read_only=True)

    class Meta:
        model = Kelembagaan
        fields = ("id", "name", "user_kelembagaan")


class JabatanSerializers(serializers.ModelSerializer):

    class Meta:
        model = Jabatan
        fields = "__all__"
