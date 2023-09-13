from rest_framework import serializers
from movies.models import Character,Movie

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "person", "character", "movie")


class MovieSerializer(serializers.ModelSerializer):
    actors = Movie.get_acotrs(Movie.actors.)
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "director", "rev")