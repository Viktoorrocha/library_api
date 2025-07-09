# books/admin.py

from django.contrib import admin
from .models import Author, Book # Importe seus novos modelos

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'created_at')
    search_fields = ('name', 'biography')
    list_filter = ('created_at', 'birth_date')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'isbn', 'created_at')
    list_filter = ('author', 'publication_date', 'created_at')
    search_fields = ('title', 'description', 'isbn')
    raw_id_fields = ('author',) # Isso torna a seleção do autor mais fácil em vez de um dropdown longo