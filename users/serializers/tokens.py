from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # add custom claims
        token["user"] = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "profileImage": str(user.profileImage.url) if user.profileImage else None,
        }

        return token
