from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import views, status, viewsets
from rest.serializers import MoviesSerializer
from rest_framework.response import Response
from rest.models import Movies
import requests
import json
from django.http import Http404
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
        movies = self.get_object()
        serializer = MoviesSerializer(movies, context={"request": request})
        return Response(serializer.data)

class MoviesViews(APIView):
    def get_object(self):
        try:
            return Movies.objects.all()
        except Movies.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        movies = self.get_object()
        serializer = MoviesSerializer(movies, context={"request": request})
        return Response(serializer.data)