from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from .models import Companies, Advocates
from .serializers import CompaniesSerializer, AdvocatesSerializer
from rest_framework.response import Response


# Create your views here.

class AdvocatesViewSets(viewsets.ModelViewSet):
    queryset = Advocates.objects.all()
    serializer_class = AdvocatesSerializer


class CompaniesViewSets(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
