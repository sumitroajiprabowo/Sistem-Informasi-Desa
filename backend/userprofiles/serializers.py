from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from .models import Profile, ProfileStatus


class ProfileAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('province', 'regency', 'district', 'village')


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users objects"""

    def get_groups(self, obj):
        return obj.groups.values_list('name', flat=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name', 'groups', 'province',
                  'regency', 'district', 'village')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 6
            }
        }

    def create(self, validated_data):
        groups_data = validated_data.pop('groups')
        user = get_user_model().objects.create_user(**validated_data)
        for group_data in groups_data:
            user.groups.add(group_data)
        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={
            'input_type': 'password'
        },
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provide credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


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
