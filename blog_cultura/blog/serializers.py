from blog.models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'nome_cultura', 'regiao', 'tema', 'idioma', 'conteudo', 'created_at']
