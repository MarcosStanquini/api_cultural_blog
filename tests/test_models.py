# blog/tests/test_models.py

import pytest
from django.utils import timezone
from blog_cultura.blog.models import Blog 

@pytest.mark.django_db
def test_blog_creation():
 
    blog = Blog.objects.create(
        nome_cultura="Cultura X",
        regiao="Região Y",
        tema="Tema Z",
        idioma="Idioma A",
        conteudo="Este é o conteúdo do blog."
    )
    
    assert blog.nome_cultura == "Cultura X"
    assert blog.regiao == "Região Y"
    assert blog.tema == "Tema Z"
    assert blog.idioma == "Idioma A"
    assert blog.conteudo == "Este é o conteúdo do blog."
    assert isinstance(blog.created_at, timezone.datetime)  
    assert blog.pk is not None  

@pytest.mark.django_db
def test_blog_creation_empty_fields(): 
    blog = Blog.objects.create(
        nome_cultura="",
        regiao="",
        tema="",
        idioma="",
        conteudo=""
    )
    

    assert blog.nome_cultura == ""
    assert blog.regiao == ""
    assert blog.tema == ""
    assert blog.idioma == ""
    assert blog.conteudo == ""
    assert isinstance(blog.created_at, timezone.datetime)  
    assert blog.pk is not None  

@pytest.mark.django_db
def test_blog_string_representation():

    blog = Blog.objects.create(
        nome_cultura="Cultura X",
        regiao="Região Y",
        tema="Tema Z",
        idioma="Idioma A",
        conteudo="Este é o conteúdo do blog."
    )
    
   
    assert str(blog) == f"{blog.nome_cultura} - {blog.tema}"
