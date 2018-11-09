from rest_framework import serializers
from livros import models


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Livro
        fields = ('codigo', 'ISBN', 'titulo', 'autor', 'ano', 'editora')
        depth = 1