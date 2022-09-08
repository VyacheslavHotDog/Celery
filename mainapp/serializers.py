from rest_framework import serializers

from mainapp.models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=200)
    count = serializers.IntegerField()
    description = serializers.CharField(max_length=1000, allow_null=True)

    def update(self, instance, validated_data):
        """update the page number of the book and save"""
        instance.count = validated_data.get('count')
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.save()
        return instance

    def create(self, validated_data):
        user = Product.objects.create(**validated_data)
        return user

    def validate_count(self, value):
        if value < 0:
            raise serializers.ValidationError("Value must be >= 0 ")
        return value
