from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class MovieDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class CustomMovieListView(generics.ListCreateAPIView):
    serializer_class = CustomMovieSerializer
    queryset = CustomMovie.objects.all()

class CustomMovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomMovieSerializer
    queryset = CustomMovie.objects.all()

class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = AppUsers.objects.all()

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = AppUsers.objects.all()

class FavouriteMovieListView(generics.ListCreateAPIView):
    serializer_class = FavouiteSerializer
    queryset = FavouriteMovie.objects.all()

class FavouriteMovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FavouiteSerializer
    queryset = FavouriteMovie.objects.all()

class PlanetListView(generics.ListAPIView):
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()

class PlanetDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()

class CustomPlanetListView(generics.ListCreateAPIView):
    serializer_class = CustomPlanetSerializer
    queryset = CustomPlanet.objects.all()

class CustomPlanetDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomPlanetSerializer
    queryset = CustomPlanet.objects.all()

class FavouritePlanetListView(generics.ListCreateAPIView):
    serializer_class = FavouritePlanetSerializer
    queryset = FavouritePlanets.objects.all()

class FavouritePlanetDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FavouritePlanetSerializer
    queryset = FavouritePlanets.objects.all()

class MovieSearchView(APIView):
    def get(self, request, custom_name):
        custom_movies = CustomMovie.objects.filter(custom__icontains=custom_name)
        movie_ids = [custom_movie.movie_id for custom_movie in custom_movies]
        movies = Movie.objects.filter(id__in=movie_ids)
        if not movies:
            custom_movies = CustomMovie.objects.filter(custom__icontains=custom_name)
            movie_ids = [custom_movie.movie_id for custom_movie in custom_movies]
            movies = Movie.objects.filter(id__in=movie_ids)

        serializer = MovieSerializer(movies, many=True, context={'request': request})
        return Response(serializer.data)

class PlanetSearchView(APIView):
    def get(self, request, custom_name):
        custom_planets = CustomPlanet.objects.filter(custom_name__icontains=custom_name)
        planet_ids = [custom_planet.planet_id for custom_planet in custom_planets]
        planets = Planet.objects.filter(id__in=planet_ids)
        if not planets:
            custom_planets = CustomPlanet.objects.filter(custom_name__icontains=custom_name)
            planet_ids = [custom_planet.planet_id for custom_planet in custom_planets]
            planets = Planet.objects.filter(id__in=planet_ids)
        serializer = PlanetSerializer(planets, many=True, context={'request': request})

        return Response(serializer.data)