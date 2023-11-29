from rest_framework import serializers
from passagens.models import ClasseViagem, Passagem, Pessoa

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasseViagem
        fields = '__all__'

class PassagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passagem
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        exclude = []
