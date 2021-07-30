from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Animal
from .serializers import AnimalSerializer

# ---------------------------------------


class AnimalView(APIView):
    def post(self, request):
        # TODO: receber a request, separar por sessão(Group, Animal e Characteristic)
        # TODO: para Group e Characteristic, verificar se existe, caso não criar
        # TODO: retornar o animal criado, 201
        print(request.data)
        return Response({"message": "Hello, World!"})

    def get(self, request, animal_id=""):
        # TODO: verificar se id não é vazio, se não for buscar pelo id
        # TODO: senão listar toda a base
        # TODO: verificar as formatações de retorno, 200
        animals = Animal.objects.all()

        serializer = AnimalSerializer(animals, many=True)

        return Response(serializer.data)

    def delete(self, request, animal_id=""):
        # TODO: verificar se id existe, caso não retornar erro, senão deletar e retornar 204
        print(request.data)
        return Response({"message": "Hello, World!"})
