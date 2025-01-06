from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'city', 'state', 'zip_code']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']
