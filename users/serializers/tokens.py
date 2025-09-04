from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # add custom claims
        token["user"] = {"id": user.id, "username": user.username}

        return token
