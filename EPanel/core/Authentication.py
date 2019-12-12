from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth import authenticate
import datetime

class JSONWebTokenAPIOverride(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            tmp_response = {}
            params = request.data
            user = authenticate(username=params['username'], password=params['password'])
            if user:
                refresh = RefreshToken.for_user(user)
                user.last_login = datetime.datetime.now()
                user.save()
                tmp_response = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
                return Response(tmp_response, status=status.HTTP_200_OK)
            else:
                return Response({
                    "message": "Wrong username or password", "message_fa": "نام کاربری یا کلمه ی عبور صحیح نیست."
                }, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
