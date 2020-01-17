from django.db import models
from django.utils.safestring import mark_safe


class Book(models.Model):
    title = models.CharField(verbose_name='Название книги', max_length=30)
    BOOKS_GENRES = [
        ('NOVEL', 'Роман' ),
        ('ADVENTURE', 'Приключенчиская литература'),
        ('SATIRE', 'Сатира'),
        ('DETECTIVE', 'Детектив'),
        ('DRAMA', 'Драма')
    ]
    genre = models.CharField(verbose_name='Жанр книги', max_length=30, choices=BOOKS_GENRES)
    author = models.CharField(verbose_name='Автор книги', max_length=30)
    date_release = models.DateField(verbose_name='Дата издания')
    language = models.SlugField(verbose_name='Язык книги')
    cover = models.URLField(verbose_name='Обложка книги')
    description = models.TextField(verbose_name='Описание книги')


    def __str__(self):
        return f'{self.title} - {self.author}'

    def book_cover(self):
        return mark_safe(f'<img> src="{self.cover}" width="100" height="100"/> ')


# class Genre(models.Model):
#     genre = models.CharField(verbose_name='Жанр книги', max_length=30, choices=)

# Create your models here.
