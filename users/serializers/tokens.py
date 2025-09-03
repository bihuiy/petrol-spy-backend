from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # add custom claims
        token["user"] = {"id": user.id, "username": user.username}

        return token

    """ # allow user to use username or email to sign in
    def validate(self, attrs):
        identifier = attrs.get("identifier")
        password = attrs.get("password")
        if not identifier or not password:
            raise self.fail("no_active_account")

        user_obj = (
            User.objects.filter(email=identifier).first()
            or User.objects.filter(username=identifier).first()
        )
        if user_obj:
            credentials = {"username": user_obj.username, "password": password}
        else:
            raise self.fail("no_active_account")

        return super().validate(credentials)

    username_field = "identifier" """
