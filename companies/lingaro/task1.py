"""
serializer
"""
from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    # add code here
    class Meta:
        model = Person
        fields = [
            'id', 'first_name', 'last_name', 'email', 'created_date'
        ]


"""
models
"""
from django.db import models


class Person(models.Model):
    # DO NOT EDIT
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=7)
    created_date = models.DateTimeField()

"""
views
"""
from rest_framework import viewsets
from rest_framework import permissions

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed.
    """
    # add code here
    queryset = Person.objects.order_by('-created_date')
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]