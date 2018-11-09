from livros import models
from api_rest import serializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class LivroListServiceView(generics.ListCreateAPIView):
    queryset = models.Livro.objects.all()
    serializer_class = serializers.LivroSerializer

class CadastrarLivroServiceView(APIView):

    def post(self, request, format=None):

        codigo = request.data.get('codigo')
        ISBN = request.data.get('ISBN')
        titulo = request.data.get('titulo')
        autor = request.data.get('autor')
        ano = request.data.get('ano')
        editora = request.data.get('editora')

        livro = models.Livro.objects.create(codigo = codigo, ISBN = ISBN, titulo = titulo, 
        									autor = autor, ano = ano, editora = editora)

        serializer = serializers.LivroSerializer(livro)
        return Response(serializer.data)

class AtualizarLivroServiceView(APIView):

    def post(self, request, format=None):

        livro = models.Livro.objects.get(codigo=request.data.get('codigo'))
        livro.ISBN = request.data.get('ISBN')
        livro.titulo = request.data.get('titulo')
        livro.autor = request.data.get('autor')
        livro.ano = request.data.get('ano')
        livro.editora = request.data.get('editora')

        livro.save()

        serializer = serializers.LivroSerializer(livro)
        return Response(serializer.data)

class ExcluirLivroServiceView(APIView):

    def post(self, request, format=None):

        livro = models.Livro.objects.get(codigo=request.data.get('codigo'))
        livro.delete()

        serializer = serializers.LivroSerializer(livro)
        return Response(serializer.data)        