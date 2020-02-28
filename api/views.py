from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from api.models import Attacks
from api.serializers import AttacksSerializer


class AttacksViewSet(viewsets.ModelViewSet):
    queryset = Attacks.objects.all().order_by('date')
    serializer_class = AttacksSerializer
