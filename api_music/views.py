
from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
from django.http import HttpResponse

def Home (request): 
    return HttpResponse("api home page")

# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()  #what do we want to return? queryset returns all of the room objects
    serializer_class = RoomSerializer

#lets us view list of all diff rooms