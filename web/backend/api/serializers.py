from rest_framework import serializers
from .models import Actor, Film

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("actor_id", "first_name", "last_name", "last_update")

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = (
                    "film_id",
                    "title",
                    "description",
                    "release_year",
                    "language",
                    "rental_duration",
                    "rental_rate",
                    "length",
                    "replacement_cost",
                    "rating",
                    "last_update",
                    "special_features",
                    "fulltext",
                  )
