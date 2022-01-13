import imp
from re import search
from rest_framework import viewsets, filters
from .serializers import ProgramaSerializer
from .models import Programa
# from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']
    filterset_fields = ['tipo', 'data_lancamento']