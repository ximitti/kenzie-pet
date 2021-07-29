from rest_framework import serializers
from animal.models import Animal

# ------------------------------------


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    scientific_name = serializers.CharField()

    animals = Animal(many=True)
