from rest_framework import serializers
from .models import Profile, ProfileStatus


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    province = serializers.StringRelatedField(read_only=True)
    regency = serializers.StringRelatedField(read_only=True)
    district = serializers.StringRelatedField(read_only=True)
    village = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class ProfileAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ("avatar",)


class ProfileStatusSerializer(serializers.ModelSerializer):

    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = "__all__"
