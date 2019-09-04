from .models import Movies
from rest_framework import serializers

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("id",)