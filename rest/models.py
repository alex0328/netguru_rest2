from django.db import models

# Create your models here.
class Raitings(models.Model):
    Source = models.CharField(max_length=300)
    Value = models.CharField(max_length=300)

class Movies(models.Model):
    Title = models.CharField(max_length=300)
    Year = models.IntegerField()
    Rated = models.CharField(max_length=300)
    Released = models.CharField(max_length=300)
    Runtime = models.CharField(max_length=300)
    Genre = models.CharField(max_length=300)
    Director = models.CharField(max_length=300)
    Writer = models.CharField(max_length=300)
    Actors = models.CharField(max_length=300)
    Plot = models.CharField(max_length=300)
    Language = models.CharField(max_length=300)
    Country = models.CharField(max_length=300)
    Awards = models.CharField(max_length=300)
    Poster = models.CharField(max_length=300)
    #Ratings = models.ForeignKey(Raitings, on_delete=models.CASCADE)
    Metascore = models.CharField(max_length=300)
    imdbRating = models.CharField(max_length=300)
    imdbVotes = models.CharField(max_length=300)
    imdbID = models.CharField(max_length=300)
    Type = models.CharField(max_length=300)
    DVD = models.CharField(max_length=300)
    BoxOffice = models.CharField(max_length=300)
    Production = models.CharField(max_length=300)
    Website = models.CharField(max_length=300)
    Response = models.CharField(max_length=300)

class Film(models.Model):
    tytul = models.CharField(max_length=30)
    opis = models.CharField(max_length=300)
    is_true = models.BooleanField(default=True)
