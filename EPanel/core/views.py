from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from EPanel.core.models import Device, Home, Section
from django.db.utils import IntegrityError
from EPanel.core.serializers import DeviceSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from .models import Demand_supply
from .serializers import DS_Serializer, HomeSerializer, SectionSerializer


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

class PlanView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):



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


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        home = Home.objects.create(owner=user)
        print(type(home))
        return Response({'msg': 'home successfully created!'})

    def get(self, request):
        user = request.user
        homes = Home.objects.filter(owner=user)
        serializer = HomeSerializer(homes, many=True)
        serialized_data = {'data': serializer.data}

        return Response(serialized_data)


class SectionView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        result = dict()
        user = request.user
        home_id = request.data['home_id']

        try:
            home = Home.objects.get(pk=home_id)
        except:
            result = {"error": "access very denied!"}
            return Response(result)

        if home.owner == user:
            my_object = Section.objects.create(home=home)
            result = {"msg": "section added to requested home!"}

        else:
            result = {"error": "access denied!"}
        return Response(result)

    def get(self, request):
        user = request.user
        homes = Home.objects.filter(owner=user)
        sections = Section.objects.filter(home__in=homes)
        serializer = SectionSerializer(sections, many=True)
        serialized_data = {'data': serializer.data}

        return Response(serialized_data)



@api_view(["POST"])
def signup(request):
    params = request.data
    username = params['username']
    password = params['password']

    user, is_new = User.objects.get_or_create(username=username)
    print(user, is_new)
    if is_new:
        user.set_password(password)
        user.save()
        return Response({'msg': "user successfully created!"})
    else:
        return Response({"error": "duplicate username,choose another one."})
