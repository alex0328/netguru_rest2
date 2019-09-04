from .models import Movies
from rest_framework import serializers

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("Title",)

class GetMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("Title",
                  "Year",
                  "Rated",
                  "Released",
                  "Runtime",
                  "Genre",
                  "Director",
                  "Writer",
                  "Actors",
                  "Plot",
                  "Language",
                  "Country",
                  "Awards",
                  "Poster",
                  "Metascore",
                  "imdbRating",
                  "imdbVotes",
                  "imdbID",
                  "Type",
                  "DVD",
                  "BoxOffice",
                  "Production",
                  "Website",
                  "Response",)