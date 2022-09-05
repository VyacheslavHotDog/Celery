from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    count = serializers.IntegerField()
    description = serializers.CharField(max_length=1000)
