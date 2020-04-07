from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer


class CustomTokenPairView(TokenObtainPairView):
    """
    Send custom claims in each token by importing and
    subclassing with the original serializer.
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
