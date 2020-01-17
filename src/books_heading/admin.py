from .models import Book
from django.contrib import admin


class AdminBook(admin.ModelAdmin):

    list_display = ['title', 'author', 'genre', 'book_cover']


admin.site.register(Book, AdminBook)
# Register your models here.
