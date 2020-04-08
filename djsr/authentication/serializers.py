from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from authentication import models


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializing custom claims.
    """
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        return token

# __TODO__  FullRegisterUserSerializer
class SimpleRegisterUserSerializer(serializers.ModelSerializer):
    # When you feed data to a model serializer like we are doing here,
    # as long as the serializer has a create() or update() method,
    # you can use serializer.save() to magically create (or update)
    # the corresponding object (in our case, CustomUser) and return
    # the instance
    """
    New Users register with email and password
    """
    email = serializers.EmailField(
        required=True
    )
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = models.CustomUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
