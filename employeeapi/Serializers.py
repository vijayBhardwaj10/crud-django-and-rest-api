from dataclasses import field

from itsdangerous import Serializer
from rest_framework import serializers

from .models import employee


class employeeSerializers(Serializer.ModelSerializers):
    class meta:
        model =employee
        fields = '__All__'
