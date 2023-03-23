from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AppUsers)
admin.site.register(Movie)
admin.site.register(FavouriteMovie)
admin.site.register(CustomMovie)
admin.site.register(Planet)
admin.site.register(FavouritePlanets)
admin.site.register(CustomPlanet)
