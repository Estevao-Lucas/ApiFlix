from django.db import models
from rest_framework import serializers
from .models import Programa


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        exclude = []