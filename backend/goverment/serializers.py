from rest_framework import serializers
from .models import Kelembagaan, Jabatan, Pemerintahan


class KelembagaanSerializers(serializers.ModelSerializer):

    class Meta:
        model = Kelembagaan
        fields = ('id', 'name',)


class JabatanSerializers(serializers.ModelSerializer):

    class Meta:
        model = Jabatan
        fields = "__all__"


class PemerintahanSerializers(serializers.ModelSerializer):

    # kelembagaan = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Kelembagaan.objects.all()
    # )
    # jabatan = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Jabatan.objects.all()
    # )
    # kelembagaan = KelembagaanSerializers(many=True)
    # jabatan = JabatanSerializers(many=True)

    # class Meta:
    #     model = Pemerintahan
    #     read_only_fields = ('id', 'user')
    #     fields = "__all__"
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Pemerintahan
        read_only_fields = ('id', 'user',)
        fields = ('id', 'kelembagaan', 'jabatan', 'name', 'user', )


class VillageGovermentSerializers(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Pemerintahan
        fields = "__all__"
