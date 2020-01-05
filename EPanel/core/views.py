from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Demand_supply
from .serializers import DS_Serializer

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'bye, World!'}
        return Response(content)

class ListDemands(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):

        homeIDs = Demand_supply.objects.all()
        serializer = DS_Serializer(homeIDs, many=True)
        serialized_data = { 'data':serializer.data}
        return Response(serialized_data)

