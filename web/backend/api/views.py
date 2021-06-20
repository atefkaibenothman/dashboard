from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import ActorSerializer, FilmSerializer
from .models import Actor, Film

class ActorView(viewsets.ModelViewSet):
    """
    API endpoint that allows actors to be viewed or edited
    """
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

class FilmView(viewsets.ModelViewSet):
    """
    API endpoint that allows films to be viewed or edited
    """
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
