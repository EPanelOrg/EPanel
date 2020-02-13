from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from EPanel.core.models import *
from django.db.utils import IntegrityError
from EPanel.core.serializers import DeviceSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render, redirect
from .models import Demand_supply
from .serializers import DS_Serializer, HomeSerializer, SectionSerializer, ProfileSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(type(request.user))
        return Response({})


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

    def post(self, request):
        pass


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


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data

        res, created = Profile.objects.get_or_create(user=request.user, email=data['email'], credit=data['credit'])
        if created:
            content = {'msg': 'profile created successfully!'}
        else:
            content = {'error': 'user profile already exists! maybe you want to modify it?'}

        return Response(content)

    def get(self, request):
        user = request.user
        if Profile.objects.filter(user=user).exists():
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile)
            data = {'data': serializer.data}
        else:
            data = {'error': 'no profile to retrieve!'}

        return Response(data)

    def put(self, request):
        user = request.user
        if Profile.objects.filter(user=user).exists():
            profile = Profile.objects.get(user=user)
            profile.email = request.data['email']
            profile.credit = request.data['credit']
            profile.save()
            content = {'msg': 'profile updated successfully!'}
        else:
            content = {'error': 'you should add profile for this user first!'}

        return Response(content)

    def delete(self, request):
        user = request.user
        if Profile.objects.filter(user=user).exists():
            Profile.objects.get().delete()
            content = {'msg': 'profile deleted successfully!'}
        else:
            content = {'error': 'no profile to delete!'}

        return Response(content)


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


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_credit(request):
    user = request.user
    credit = Profile.objects.get(user=user).credit
    content = {'credit-amount': credit}

    return Response(content)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_homes(request):
    homes = Home.objects.all()

    content = {'homes-count': len(homes)}

    return Response(content)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_usage(request):
    user = request.user
    homes = Home.objects.filter(owner=user)
    user_daily_usage = 0
    for home in homes:
        user_daily_usage += home.get_home_daily_usage()

    content = {
        'users_daily_usage': user_daily_usage
    }

    return Response(content)
