from employeeapi import serializers
from rest_framework import viewsets
from .import models
from .import Serializers

class employeeviewset(viewsets.modelviewset):
    queryset = models.employee.objects.all()
    Serializers_class = serializers.employeeserializer
