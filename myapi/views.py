from django.shortcuts import render
from rest_framework import serializers, viewsets

from .serializers import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializers_class = UserSerializer
    