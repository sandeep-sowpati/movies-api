from rest_framework import serializers
from .models import *

class FavouiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavouriteMovie
        fields = "__all__"

class CustomMovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomMovie
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True,read_only=True, view_name='movie-detail')
    planets = serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='planet-detail')
    class Meta:
        model = AppUsers
        fields = '__all__'

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    movieusers = serializers.HyperlinkedRelatedField(many=True,read_only=True, view_name='appusers-detail')
    customname = serializers.HyperlinkedRelatedField(many=True,read_only=True, view_name = 'custommovie-detail' )
    class Meta:
        model = Movie
        fields = '__all__'

class FavouritePlanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavouritePlanets
        fields = '__all__'

class CustomPlanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomPlanet
        fields = '__all__'

class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    planetusers = serializers.HyperlinkedRelatedField(many=True,read_only=True, view_name='appusers-detail')
    customplanet = serializers.HyperlinkedRelatedField(many=True,read_only=True, view_name = 'custommovie-detail' )
    class Meta:
        model = Planet
        fields = '__all__'