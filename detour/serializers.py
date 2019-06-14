from rest_framework import serializers
from .models import Map, Detour


class MapSerializer(serializers.HyperlinkedModelSerializer):
    detours = serializers.HyperlinkedRelatedField(
        view_name='detour_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Map
        fields = ('id', 'title', 'city', 'country', 'description', 'detours')


class DetourSerializer(serializers.HyperlinkedModelSerializer):
    map = serializers.HyperlinkedRelatedField(
        view_name='map_detail',
        read_only=True
    )

    class Meta:
        model = Detour
        fields = ('id', 'map', 'name', 'lat', 'lng', 'notes')

    def create(self, validated_data):
        detour = Detour.objects.create(validated_data)
