from rest_framework.views import APIView
from rest_framework.response import Response
from plataforma.models import Mensagens
from usuario.models import Contatos
from .serializers import MensagensSerializer, ContatosSerializer

# Create your views here.
class Mensagem(APIView):
    def get(self, request):
        mensagens = Mensagens.objects.all()
        serializer = MensagensSerializer(mensagens, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MensagensSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

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