from django.core.management.base import BaseCommand
from datetime import datetime
import requests
from nsap.models import Planet, Movie

class Command(BaseCommand):
    help = 'Fetches data from Star Wars API and saves it to the database'

    def handle(self, *args, **kwargs):
        # Fetch planets data
        planets_url = 'https://sw-api-rwjfuiltyq-el.a.run.app/api/planets'
        planets_data = requests.get(planets_url).json()['results']
        for planet_data in planets_data:
            planet = Planet(
                name=planet_data['name'],
                created=datetime.fromisoformat(planet_data['created'].replace('Z', '+00:00')),
                edited=datetime.fromisoformat(planet_data['edited'].replace('Z', '+00:00')),
                url=planet_data['url'],
            )
            planet.save()

        # Fetch movies data
        movies_url = 'https://sw-api-rwjfuiltyq-el.a.run.app/api/films'
        movies_data = requests.get(movies_url).json()['results']
        for movie_data in movies_data:
            movie = Movie(
                title=movie_data['title'],
                episode_id=movie_data['episode_id'],
                opening_crawl=movie_data['opening_crawl'],
                director=movie_data['director'],
                producer=movie_data['producer'],
                release_date=datetime.fromisoformat(movie_data['release_date'].replace('Z', '+00:00')),
                created=datetime.fromisoformat(movie_data['created'].replace('Z', '+00:00')),
                edited=datetime.fromisoformat(movie_data['edited'].replace('Z', '+00:00')),
                url=movie_data['url'],
            )
            movie.save()