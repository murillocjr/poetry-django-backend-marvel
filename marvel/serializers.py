from rest_framework import serializers
from marvel.models import LoginRequestDTO


class LoginRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginRequestDTO
        fields = "__all__"
