from django.db import models

'''Common models between Movies and Planet'''

class AppUsers(models.Model):
    '''Model for all user Registration'''
    username = models.CharField(max_length=100)
    age = models.IntegerField()

'''
All models related to Movies
'''
class Movie(models.Model):
    '''Model for Movie Details'''
    title = models.CharField(max_length=200)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField()
    director = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    release_date = models.DateField()
    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

class FavouriteMovie(models.Model):
    '''Model to add movies as favourites'''
    movie_user = models.ForeignKey(
        AppUsers, on_delete=models.CASCADE, related_name= 'movies'
    )
    movie = models.ForeignKey(
        Movie, on_delete= models.CASCADE, related_name= 'movieusers'
    )


class CustomMovie(models.Model):
    '''Model for Custom movie name'''
    movie = models.ForeignKey(
        Movie, on_delete= models.CASCADE, related_name= 'customname'
    )
    custom = models.CharField(max_length=100)


'''
All Models realted to planet
'''

class Planet(models.Model):
    '''Model for Planet'''
    name = models.CharField(max_length=100)
    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.name


class FavouritePlanets(models.Model):
    '''Model for favourite Planets'''
    planet_user = models.ForeignKey(
        AppUsers, on_delete=models.CASCADE, related_name='planets'
    )
    planet = models.ForeignKey(
        Planet, on_delete= models.CASCADE, related_name='planetusers'
    )

class CustomPlanet(models.Model):
    '''Model for Custom planet name'''
    planet = models.ForeignKey(
        Planet, on_delete= models.CASCADE, related_name='customplanet'
    )
    custom_name = models.CharField(max_length=100)
