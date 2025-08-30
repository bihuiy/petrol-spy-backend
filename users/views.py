from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.common import AuthSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


# Create your views here.
# Sign up
# Path: /users/sign-up
class SignUpView(APIView):
    def post(self, request):
        serialized_user = AuthSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()

        user = User.objects.get(pk=serialized_user.data["id"])
        refresh = RefreshToken.for_user(user)
        return Response({"access": str(refresh.access_token)}, 201)
