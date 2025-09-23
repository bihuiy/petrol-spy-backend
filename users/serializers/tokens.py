from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from ..models import User


class TokenSerializer(TokenObtainPairSerializer):
    username_field = "identifier"

    def validate(self, attrs):
        identifier = attrs.get("identifier")
        password = attrs.get("password")

        if not identifier or not password:
            raise AuthenticationFailed("Both identifier and password are required.")

        try:
            user = User.objects.get(username=identifier)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=identifier)
            except User.DoesNotExist:
                raise AuthenticationFailed(
                    "No active account found with the given credentials"
                )

        if not user.check_password(password):
            raise AuthenticationFailed(
                "No active account found with the given credentials"
            )

        refresh = self.get_token(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

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
