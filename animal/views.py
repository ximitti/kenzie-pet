from django.db.models import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Animal
from group.models import Group
from characteristic.models import Characteristic

from .serializers import AnimalSerializer

# ---------------------------------------


class AnimalView(APIView):
    def post(self, request) -> Response:
        serialized = AnimalSerializer(data=request.data)

        if not serialized.is_valid():
            return Response(serialized.error, status=status.HTTP_400_BAD_REQUEST)

        animal_data = serialized.validated_data
        group_data = animal_data.pop("group")
        characteristics_data = animal_data.pop("characteristics")

        group: Group = Group.objects.get_or_create(**group_data)[0]

        animal: Animal = Animal.objects.create(**animal_data, group=group)

        characteristics: list[Characteristic] = [
            Characteristic.objects.get_or_create(**characteristic)[0]
            for characteristic in characteristics_data
        ]

        animal.characteristics.set(characteristics)

        serialized = AnimalSerializer(animal)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def get(self, request, animal_id="") -> Response:
        if animal_id:
            try:
                animal: Animal = Animal.objects.get(id=animal_id)

                serialized: AnimalSerializer = AnimalSerializer(animal)

                return Response(serialized.data, status=status.HTTP_200_OK)

            except ObjectDoesNotExist as _:
                return Response(
                    {"detail": "Animal not found"}, status=status.HTTP_404_NOT_FOUND
                )

        animals: list[Animal] = Animal.objects.all()

        serialized: list[AnimalSerializer] = AnimalSerializer(animals, many=True)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def delete(self, request, animal_id="") -> Response:
        try:
            animal: Animal = Animal.objects.get(id=animal_id)

            animal.delete()

            return Response("", status=status.HTTP_204_NO_CONTENT)

        except ObjectDoesNotExist as _:
            return Response(
                {"detail": "Animal not found"}, status=status.HTTP_404_NOT_FOUND
            )

        except ValueError as _:
            return Response(
                {"detail": "Missing parameter id"}, status=status.HTTP_400_BAD_REQUEST
            )
