from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Animal
from .serializers import AnimalSerializer

# ---------------------------------------


class AnimalView(APIView):
    def post(self, request):
        print(request.data)
        return Response({"message": "Hello, World!"})

    def get(self, request, animal_id=""):
        animals = Animal.objects.all()
        print(animals)

        serializer = AnimalSerializer(animals, many=True)

        return Response(serializer.data)

    def delete(self, request):
        print(request.data)
        return Response({"message": "Hello, World!"})
