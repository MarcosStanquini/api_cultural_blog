from django.db import models

class Blog(models.Model):
    nome_cultura = models.CharField(max_length=120)
    regiao = models.CharField(max_length=120)
    tema = models.CharField(max_length=120)
    idioma = models.CharField(max_length=120)
    conteudo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)