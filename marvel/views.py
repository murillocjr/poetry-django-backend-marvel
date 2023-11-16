from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from marvel.models import Film
from marvel.serializers import FilmSerializer, LoginRequestSerializer


class FilmList(APIView):
    def get(self, request, format=None):
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)
	
    def post(self, request, format=None):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request, format=None):
        serializer = LoginRequestSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.data["username"] == "admin" and serializer.data["password"] == "123456":
                return Response({"status": "success", "code": 200, "data": { "username": "user-user", "devicename": "android", "genericname": "demo"} }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

