from rest_framework import generics
from .serializers import MapSerializer, DetourSerializer
from .models import Map, Detour


class MapList(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class DetourList(generics.ListCreateAPIView):
    queryset = Detour.objects.all()
    serializer_class = DetourSerializer


class DetourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detour.objects.all()
    serializer_class = DetourSerializer
