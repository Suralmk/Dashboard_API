from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions, status
from rest_framework.generics import (ListAPIView,  CreateAPIView)
from rest_framework.views import APIView
from .serializers import StatsticsListSerializer, DashboardDataSerializer,AddstatsticsDataSeriaizer
from . models import Statstics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        return token

class MyTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(["GET"])
def index(request):
    return Response({"Assignment": "BlackCoffer Assignment backend API"})

class AddstatsticsData(APIView):

    def post(self, request):
        data = request.data
        for d in data:
            serializer = AddstatsticsDataSeriaizer(data=d, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        response = {
                "message": "Data Created Succefully",
                "created": True 
        }   
        return Response(response, status=status.HTTP_201_CREATED)

class StatsticsListView(ListAPIView):
    serializer_class = StatsticsListSerializer
    queryset = Statstics.objects.all()
    permission_classes = [permissions.AllowAny]

class DashboardDataView(APIView):
    
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        query = Statstics.objects.all()
        data = DashboardDataSerializer(query).data
        return Response(data, status=status.HTTP_200_OK)