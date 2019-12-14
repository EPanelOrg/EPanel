from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from EPanel.core.models import BlackListedToken
from EPanel.core.Utils import IsTokenValid
from django.db.utils import IntegrityError


class HelloView(APIView):
    permission_classes = (IsAuthenticated, IsTokenValid)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class LogOut(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        content = {"msg": 'trying to log-out you...'}
        try:
            blacklistentry = BlackListedToken(token=request.auth, user_id=request.user.id)
            blacklistentry.save()
        except IntegrityError:
            content = {"msg": "already logged-out!"}
        return Response(content)