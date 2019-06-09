from rest_framework import serializers
from .models import Collection, Favorite


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    favorites = serializers.HyperlinkedRelatedField(
        view_name='favorite_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Collection
        fields = ('id', 'name', 'city', 'country', 'favorites')


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    collection = serializers.HyperlinkedRelatedField(
        view_name='collection_detail',
        read_only=True
    )

    class Meta:
        model = Favorite
        fields = ('id', 'collection', 'name', 'lat', 'long', 'notes')
