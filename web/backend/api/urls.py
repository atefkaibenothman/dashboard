from django.urls import path
from graphene_django.views import GraphQLView

from api.schema import schema as graphql_schema

urlpatterns = [
            # only a single URL to access GraphQL
            path("", GraphQLView.as_view(graphiql=True, schema=graphql_schema)),
        ]
