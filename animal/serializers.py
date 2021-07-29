from rest_framework import serializers

from group.models import Group
from characteristic.models import Characteristic

# -----------------------------------


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()

    group = Group()

    characteristics = Characteristic(many=True)
