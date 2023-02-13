#serializers ajudam a criar/salvar models
from django.forms import ValidationError
from rest_framework import serializers
from teacher.models import Professor, Aula


#responsável por transformar o modelo em um objeto json
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor #qual model
        fields = '__all__' #quais campos serializar


#serializer somente para retornar as informações do aluno quando ele se cadastrar na aula
class CadastrarAulaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length = 100)
    email = serializers.EmailField(max_length = 255)

    def validate_nome(self,value):
        if len(value) < 3:
            raise ValidationError('O nome deve ter ao menos três caracteres.')
        else:
            return value

    def validate_email(self,value):
        if '@' not in value:
            raise ValidationError('Email inválido.')
        else: 
            return value


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'