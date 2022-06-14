from rest_framework.views import APIView
from rest_framework.response import Response
from usuario.models import Contatos
from apis.serializers import ContatosSerializer

# Create your views here.

class Contato(APIView):
    def get(self, request):
        contatos = Contatos.objects.all()
        serializer = ContatosSerializer(contatos, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ContatosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)