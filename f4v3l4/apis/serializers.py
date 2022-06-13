from rest_framework import serializers
from plataforma.models import Mensagens
from usuario.models import Contatos

class MensagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagens
        fields = '__all__'

class ContatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contatos
        fields = '__all__'