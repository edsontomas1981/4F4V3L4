from rest_framework.views import APIView
from rest_framework.response import Response
from plataforma.models import Mensagens
from apis.serializers import MensagensSerializer

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