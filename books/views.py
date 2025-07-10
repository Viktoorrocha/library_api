# books/views.py 

from rest_framework import viewsets
from .models import Book, Author
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que os autores sejam visualizados ou editados.
    """
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite que os livros sejam visualizados ou editados.
    """
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer