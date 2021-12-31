from rest_framework import serializers


class Helloserializer(serializers.Serializer):
    """ Serialises a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
