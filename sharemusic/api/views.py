from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Room
from .serializers import roomSerializer

# Create your views here.
def main(request):
  return HttpResponse("Hello, World!")

def home(request):
  return HttpResponse("welcome to home")

class RoomSerializerView(generics.CreateAPIView):
  queryset= Room.objects.all()
  serializer_class=roomSerializer