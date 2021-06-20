from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import ActorSerializer
from .models import Actor

class ActorView(viewsets.ModelViewSet):
    """
    API endpoint that allows actors to be viewed or edited
    """
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
