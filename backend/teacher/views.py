#importar APIview para conseguir dar display nas informações json
import email
from rest_framework.views import APIView
#Response para dar o return no final das funções
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

#importando o get_or_404 pra lançar um 404 padrão se a busca pelo ID do professor der erro
from django.shortcuts import get_object_or_404


from teacher.models import Aula, Professor
from teacher.serializers import ProfessorSerializer, CadastrarAulaSerializer, AulaSerializer

#o APIview que será retornado tem que ser uma classe herdada de APIView
class IndexApiView(APIView):
    def get(self,request,format=None):
        return Response({'Nome':'Gabriel Ricardo','idade':22},status=200)



class ProfessorApiView(APIView):
    #função que busca todos os professores cadastrados no banco de dados
    def get(self,request,format=None):
        professores = Professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True) #passando quais os objetos para transformar em json, e especificando que são muitos
        return Response(serializer.data, HTTP_200_OK )


class CadastrarAulaApiView(APIView):
    #criando a função post para criar uma rota onde o aluno se cadastra na aula
    def post(self,request,id,format = None):
        #procurando o professor com o ID selecionado
        professor = get_object_or_404(Professor, id=id)
        #capturando as informações da aula e transformando elas em json
        serializer = CadastrarAulaSerializer(data=request.data)
        #se as informações são válidas, salve a aula no bd e dê display no frontend
        if serializer.is_valid():
            aula = Aula(
                nome = serializer.validated_data.get('nome'),
                email = serializer.validated_data.get('email'),
                professor= professor
            )
            aula.save()
            aula_serializer = AulaSerializer(aula, many=False)
            return Response(aula_serializer.data, status = HTTP_201_CREATED)
        #se não, dê display nos erros e 400/Bad request
        return Response({"massage": "Houve erro na validação", "errors" : serializer.errors}, 
        status = HTTP_400_BAD_REQUEST)