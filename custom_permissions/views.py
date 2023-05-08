from django.shortcuts import render
from .serializers import CarSerialize
from .models import Cars
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from .permissions import MyPermission
# Create your views here.

class CarModelViewset(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerialize
    authentication_classes = [BasicAuthentication]
    permission_classes = [MyPermission]
    