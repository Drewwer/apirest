from django.shortcuts import render
from rest_framework import viewsets
from .models import Libro
from .serializers import LibroSerializer
# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()