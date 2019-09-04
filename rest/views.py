from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import views, status, viewsets
from rest.serializers import MoviesSerializer, GetMoviesSerializer
from rest_framework.response import Response
from rest.models import Movies
import requests
import json
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

# Create your views here.
class MoviesView(viewsets.ModelViewSet):
    def get_object(self):
        try:
            return Movies.objects.all()
        except Movies.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        return Http404
        movies = self.get_object()
        serializer = MoviesSerializer(movies, context={"request": request})
        return Response(serializer.data)

class MoviesViews(APIView):
    def get_object(self):
        try:
            return Movies.objects.get(pk=1)
        except Movies.DoesNotExist:
            raise Http404

    def get(self, request):
        movies = self.get_object()
        serializer = GetMoviesSerializer(movies)
        # if serializer.is_valid():
        #     return Response(serializer.validated_data)
        return Response(serializer.data)

    def post(self, request):
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            first_title = serializer.validated_data
            title = first_title['Title']
            print(title)
            apikey = "81b6b98e"
            service = "http://www.omdbapi.com/"
            payload = {'apikey': apikey, 't': title}
            r = requests.get(service, params=payload)
            print(r)
            response_json = r.json()
            income_response = response_json["Response"]
            if income_response:
                print(response_json["Year"])
                income_year = int(response_json["Year"])
                # income_imdbRating = int(response_json["imdbRating"])
                # income_imdbVotes = int(response_json["imdbVotes"])
                film_add = Movies(Title=response_json["Title"],
                                  Year=income_year,
                                  Rated=response_json["Rated"],
                                  Released=response_json["Released"],
                                  Runtime=response_json["Runtime"],
                                  Genre=response_json["Genre"],
                                  Director=response_json["Director"],
                                  Writer=response_json["Writer"],
                                  Actors=response_json["Actors"],
                                  Plot=response_json["Plot"],
                                  Language=response_json["Language"],
                                  Country=response_json["Country"],
                                  Awards=response_json["Awards"],
                                  Poster=response_json["Poster"],
                                  Metascore=response_json["Metascore"],
                                  imdbRating=response_json["imdbRating"],
                                  imdbVotes=response_json["imdbVotes"],
                                  imdbID=response_json["imdbID"],
                                  Type=response_json["Type"],
                                  DVD=response_json["DVD"],
                                  BoxOffice=response_json["BoxOffice"],
                                  Production=response_json["Production"],
                                  Website=response_json["Website"],
                                  Response=response_json["Response"],
                                  )
                film_add.save()
        #             print(response_json["Title"])
        #             print(response_json)
        #             return Response(response_json)
        #         else:
        #             return Response(response_json)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(response_json)