from rest_framework import serializers
from movies.models import Character,Movie

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "person", "character", "movie")

class CharacterMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("person", "character")

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "director","scripts", "actors" , "reviews", )

class MoviePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "director","scripts", )
        