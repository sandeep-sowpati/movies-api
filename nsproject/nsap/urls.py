from django.urls import path
from .views import *

urlpatterns = [
    path('users/',UserListView.as_view(), name = 'users'),
    path('users/<int:pk>',UserDetailsView.as_view(),name = 'appusers-detail' ),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movies/<int:pk>',MovieDetailView.as_view(),name = 'movie-detail'),
    path('planets/', PlanetListView.as_view(), name='planets'),
    path('planets/<int:pk>',PlanetDetailView.as_view(),name = 'planet-detail'),
    path('custommovie', CustomMovieListView.as_view(), name='custommovie'),
    path('custommovie/<int:pk>', CustomMovieDetailView.as_view(),name = 'custommovie-detail'),
    path('customplanet', CustomPlanetListView.as_view(), name='customplanet'),
    path('customplanet/<int:pk>', CustomPlanetDetailView.as_view(),name = 'customplanet-detail'),
    path('favourites/movies', FavouriteMovieListView.as_view(),name = 'favourites Movies'),
    path('favourites/movies/<int:pk>', FavouriteMovieDetailView.as_view() , name='favouritemovie-detail'),
    path('favourites/planets/', FavouritePlanetListView.as_view(),name = 'favourite Planet'),
    path('favourites/planets/<int:pk>', FavouritePlanetDetailView.as_view(),name = 'favouriteplanets-detail'),
    path('movies/search/<str:custom_name>/', MovieSearchView.as_view(), name='Search Movie'),
    path('planet/search/<str:custom_name>', PlanetSearchView.as_view(), name='Search planet')
]