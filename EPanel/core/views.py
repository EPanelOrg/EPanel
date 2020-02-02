from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from EPanel.core.models import Device
from django.db.utils import IntegrityError
from EPanel.core.serializers import DeviceSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from .models import Demand_supply
from .serializers import DS_Serializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'bye, World!'}
        return Response(content)


class DeviceView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        content = dict()
        consuming_power = request.data['consuming_power']
        device_name = request.data['device_name']
        try:
            res = Device.objects.create(consuming_power=consuming_power, device_name=device_name)
            content = {"msg": "ok"}
        except IntegrityError as ex:
            print(ex)
            content = {"error": "IntegrityError", "msg": "device with such name exists, maybe you want to delete or "
                                                         "edit existing one?"}

        return Response(content)

    def get(self, request, pk=None):
        if pk:
            device_name = pk
            try:
                res = Device.objects.get(device_name=device_name)
                serializer_class = DeviceSerializer(res)
                serialized_data = {'data': serializer_class.data}['data']
                content = serialized_data

            except Exception as ex:
                print(ex)
                content = {"error": str(ex), "msg": "no device with such a device_name."}
        else:
            content = []
            objects = Device.objects.all()
            for object in objects:
                serializer_class = DeviceSerializer(object)
                serialized_data = {'data': serializer_class.data}['data']
                content.append(serialized_data)

        return Response(content)

    def put(self, request):
        consuming_power = request.data['consuming_power']
        device_name = request.data['device_name']
        try:
            object = Device.objects.get(device_name=device_name)
            object.consuming_power = consuming_power
            object.save()
            content = {"msg": "ok"}
        except Exception as ex:
            print(ex)
            content = {"error": str(ex)}

        return Response(content)

    def delete(self, request):
        device_name = request.data['device_name']
        try:
            object = Device.objects.get(device_name=device_name)
            object.delete()
            content = {"msg": "ok"}
        except Exception as ex:
            print(ex)
            content = {"error": str(ex)}

        return Response(content)


class ListDemands(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        homeIDs = Demand_supply.objects.all()
        serializer = DS_Serializer(homeIDs, many=True)
        serialized_data = {'data': serializer.data}
        return Response(serialized_data)

    def post(self, request):
        params = request.data
        serializer = DS_Serializer(data=params)
        result = dict()
        if serializer.is_valid():
            create_result = serializer.save()
            print(create_result)
        else:
            result['error'] = serializer.errors
        return Response(result)


@api_view(["POST"])
def signup(request):
    params = request.data
    username = params['username']
    password = params['password']

    user = User.objects.create(username= username)
    user.set_password(password)
    user.save()
    print(user)

    return Response({})