"""EPanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from EPanel.core import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.signup, name='signup'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # apis
    path('admin/', admin.site.urls),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('device/<str:pk>', views.DeviceView.as_view(), name='device'),
    path('device/', views.DeviceView.as_view(), name='device'),
    path('home-api/', views.HomeView.as_view(), name='home'),
    path('section/', views.SectionView.as_view(), name='home'),
    path('get-credit/', views.get_credit, name='credit'),
    path('get-homes/', views.get_homes, name='homes'),
    path('my-usage/', views.user_usage, name='user usage'),
    path('main/', views.main_page, name='main page'),
    path('dashboard/', views.dashboard, name='main page'),

    path('home/', views.homes, name='main page'),

    path('profile-api/', views.ProfileView.as_view(), name='credit'),
    path('ds/', views.ListDemands.as_view(), name='list'),
    path('addToAuction/', views.add_to_auction, name='join_auction'),
    path('startAuction/', views.start_auction, name='join_auction'),

    path('', views.index, name="homepage"),
    path('profile/', views.profile, name='profile'),

    # pages
    path('auction/', views.auction, name="auction")
]
