from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from asosiy.views import *
from stats.views import *
from userapp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Ombor API",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact("Xojiakbar Goipov. xojiakbargoipov3@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',schema_view.with_ui('swagger', cache_timeout=00), name='swagger-doc'),
    path('clientlar/', ClentApiView.as_view()),
    path('client/<int:pk>/', ClentApi.as_view()),
    path('mahsulotlar/',MahsulotApiView.as_view()),
    path('stats/', StetsApiView.as_view()),
    path('stat/<int:pk>/', StetsApi.as_view()),
    path('user/<int:pk>', UserView.as_view()),
    path('userlar/', Userlar.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token-ber'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_yangila'),
]




