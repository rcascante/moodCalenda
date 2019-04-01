from django.shortcuts import render
from .models import GiphyCalendar
from .serializers import GiphySerializer
from rest_framework import generics

# Create your views here.
class GiphyListCreate(generics.ListAPIView):
    queryset = GiphyCalendar.objects.all()
    serializer_class = GiphySerializer
