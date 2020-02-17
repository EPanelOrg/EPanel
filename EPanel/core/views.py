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
from django.views.decorators.clickjacking import xframe_options_exempt
from .serializers import DS_Serializer
from datetime import datetime
from .algorithms import ProfitBased


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
        address = request.data['address']
        home = Home.objects.create(owner=user, address=address)
        print(type(home))
        return Response({'msg': 'home successfully created!'})

    def get(self, request):
        user = request.user
        homes = Home.objects.filter(owner=user)
        serializer = HomeSerializer(homes, many=True)
        serialized_data = {'data': serializer.data}

        return Response(serialized_data)

    def delete(self, request):

        user = request.user
        if Home.objects.filter(user=user).exists():
            Home.objects.get().delete()
            content = {'msg': 'hoem deleted successfully!'}
        else:
            content = {'error': 'no home to delete!'}

        return Response(content)

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

        res, created = Profile.objects.get_or_create(user=request.user, CitizenshipNo=data['CitizenshipNo'],
                                                     BDate=data['BDate'], lastName=data['lastName'], name=data['name'],
                                                     email=data['email'], credit=data['credit'])
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
            content = {'profileData': serializer.data}
        else:
            content = {'error': 'no profile to retrieve!'}

        return Response(content)

    def put(self, request):
        user = request.user

        if Profile.objects.filter(user=user).exists():
            profile = Profile.objects.get(user=user)
            profile.email = request.data['email']
            profile.credit = request.data['credit']
            profile.CitizenshipNo = request.data['CitizenshipNo']
            profile.BDate = request.data['BDate']
            profile.lastName = request.data['lastName']
            profile.name = request.data['name']

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
    email = params['email']

    try:
        user, is_new = User.objects.get_or_create(username=username, email=email)
        if is_new:
            user.set_password(password)
            user.save()
        return Response({"result": 1})
    except IntegrityError:
        return Response({"result": 0})


@api_view(["POST"])
def add_to_auction(request):
    permission_classes = (IsAuthenticated,)
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return Response({"result": -1})

    params = request.data
    type = params['type']
    private_price = params['private_price']
    power_amount = params["power_amount"]

    home = Home.objects.filter(owner=request.user)
    if home is None:
        Response({"result": -2})
    try:
        home.update(type=type, private_price=private_price, power_amount=power_amount)
        home.save()

        auction = Auction.objects.last()
        Auction_Home.objects.create(home=home, auction=auction, trade_price=0, traded_with=0, date_time=0, happened=0)

        return Response({"result": 1})
    except Exception as ex:
        print(ex)
        return Response({"result": 0})


@api_view(["GET"])
def start_auction(request):
    try:
        auction = Auction.objects.last()
        ahs = Auction_Home.objects.filter(auction=auction)
        homes = []
        for ah in ahs:
            homes.append({str(ah.home.home_id): {"type": str(ah.home.type), "price": ah.home.private_price,
                                                 "amount": ah.home.power_amount}})
        print(homes)
        pb = ProfitBased()
        result = pb.start(homes)
        return Response({"result": result})
    except Exception as ex:
        print(ex)
        return Response({"result": 0})


def index(request):
    return render(request, 'index.html')


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

@xframe_options_exempt
def profile(request):
    print("profile requested!")
    return render(request, 'profile.html')


def main_page(request):
    # return render(request, 'index.html', context=my_dict)
    return render(request, 'information.html')


@xframe_options_exempt
def dashboard(request):
    # return render(request, 'index.html', context=my_dict)
    return render(request, 'dashBoard.html')

@xframe_options_exempt
def homes(request):

    return render(request,'homes.html')


def auction(request):
    return render(request, 'auction.html')
