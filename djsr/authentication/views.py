from rest_framework import permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication import serializers

################################################################
class HelloWorldView(APIView):
    """
    Creating and testing a protected view.
    """
    def get(self, request):
        return Response(data={"hello":"world"}, status=status.HTTP_200_OK)
################################################################


class CustomTokenPairView(TokenObtainPairView):
    """
    Send custom claims in each token by importing and
    subclassing with the original serializer.
    """
    serializer_class = serializers.MyTokenObtainPairSerializer

class CustomUserCreate(APIView):
    """
    Creates new Users

    Required fields: email and password
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = serializers.SimpleRegisterUserSerializer(
                                                    data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
