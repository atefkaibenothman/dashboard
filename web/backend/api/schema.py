import graphene
from graphene_django import DjangoObjectType

from .models import Actor, Film

class ActorType(DjangoObjectType):
    class Meta:
        model = Actor
        fields = ("actor_id", "first_name", "last_name", "last_update")

class FilmType(DjangoObjectType):
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

class Query(graphene.ObjectType):
    all_actors = graphene.List(ActorType)
    all_films = graphene.List(FilmType)

    def resolve_all_actors(self, info):
        return Actor.objects.all()

    def resolve_all_films(self, info):
        return Film.objects.all()


schema = graphene.Schema(query=Query)

