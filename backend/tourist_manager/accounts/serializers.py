from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('account_type',)

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'profile')

class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        #user = User(username=validated_data['username'], first_name=validated_data['first_name'], last_name=validated_data['last_name']) 
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile.objects.create(user=user, **profile_data)
        user.profile = profile
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials")
