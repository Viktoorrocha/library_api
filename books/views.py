# books/views.py 

from rest_framework import viewsets
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import filters


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que os autores sejam visualizados ou editados.
    """
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'biography'] # Campos que podem ser buscados por texto
    ordering_fields = ['name', 'birth_date'] # Campos pelos quais pode ordenar
    ordering = ['name'] # Ordenação padrão: por nome 


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que os livros sejam visualizados ou editados.
    """
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'isbn'] # Campos que podem ser buscados por texto

    filterset_fields = ['author', 'publication_date'] # Campos que pode ser filtrados exatamente (DjangoFilterBackend)

    ordering_fields = ['title', 'publication_date'] # Campos pelos quais pode ordenar
    ordering = ['title']  # Ordenação padrão: por título, crescente