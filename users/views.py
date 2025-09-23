from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.common import AuthSerializer
from .models import User
from .serializers.tokens import TokenSerializer
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.
# Sign up
# Path: /users/sign-up
class SignUpView(APIView):

    def post(self, request):
        serialized_user = AuthSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        """ if not serialized_user.is_valid():
            print("Validation errors:", serialized_user.errors)  
            return Response(serialized_user.errors, status=400) """
        serialized_user.save()

        user = User.objects.get(pk=serialized_user.data["id"])
        refresh = TokenSerializer.get_token(user)
        return Response({"access": str(refresh.access_token)}, 201)
