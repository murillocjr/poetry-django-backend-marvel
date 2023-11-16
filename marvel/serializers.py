from rest_framework import serializers
from marvel.models import Film, LoginRequestDTO


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"

class LoginRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginRequestDTO
        fields = "__all__"