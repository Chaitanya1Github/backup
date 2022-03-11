from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# this is to generate token for the user which already exists in user table.
# you need to pass username and password in POST method to generate token for that particular user
# the work of token generation and refreshing is handled in app level urls.py by TokenObtainPairView and TokenRefreshView classes
class ExampleView(APIView):

    # when the following line is added you cannot access this route in browser or in postman
    # permission_classes = [IsAuthenticated]
    # print(permission_classes)
    # template_name = "app_jwt_authentication/homepage.html"

    def get(self, request):
        print(request.user)
        content = {
            # 'user': str(request.user),
            'status': 'request was permitted to view this page...',
        }
        return Response(content)
        # return render(request, self.template_name, content)


# how to generate token manually when new user registers for the first time.
from rest_framework_simplejwt.tokens import RefreshToken
class RegisterView(APIView):

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = User(username=username)
        user.set_password(password)
        refresh = RefreshToken.for_user(user)
        user.save()

        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(tokens)



