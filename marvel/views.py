from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from marvel.serializers import LoginRequestSerializer

class Login(APIView):
    def post(self, request, format=None):
        serializer = LoginRequestSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.data["username"] == "admin" and serializer.data["password"] == "123456":
                return Response({"status": "success", "code": 200, "data": {"id":"007", "username": "bond-james", "firstname": "james", "lastname": "bond"} }, status=status.HTTP_200_OK, content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

