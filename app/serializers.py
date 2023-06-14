# myapp/serializers.py

from rest_framework import serializers
from app.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'bio', 'profile_picture']
