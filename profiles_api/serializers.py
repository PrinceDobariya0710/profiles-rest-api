from unittest.util import _MAX_LENGTH
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers serializes  a name field for testing our APIView"""
    """It is very similar to django forms"""
    name = serializers.CharField(max_length=10)