from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .userDetail import UserDetailSerializer

class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # add custom claims
        token["user"] = {
            "id": user.id,
            "username": user.username,
        }

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        
        serializer = UserDetailSerializer(self.user)
        data['user'] = serializer.data
        
        return data