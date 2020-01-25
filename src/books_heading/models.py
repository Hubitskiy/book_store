from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Book(models.Model):
    title = models.CharField(verbose_name='Название книги', max_length=30, unique=True)
    author = models.CharField(verbose_name='Автор книги', max_length=30)

    BOOKS_GENRES = [
            ('NOVEL', 'Роман'),
            ('ADVENTURE', 'Приключенчиская литература'),
            ('SATIRE', 'Сатира'),
            ('DETECTIVE', 'Детектив'),
            ('DRAMA', 'Драма')
        ]

    genre = models.CharField(verbose_name='Жанр книги', choices=BOOKS_GENRES, max_length=30, null=True)
    date_release = models.DateField(verbose_name='Дата издания', null=True, blank=True)
    language = models.SlugField(verbose_name='Язык книги', null=True, blank=True)
    cover = models.URLField(verbose_name='Обложка книги', null=True, blank=True)
    description = models.TextField(verbose_name='Описание книги')


    def __str__(self):
        return f'{self.title} - {self.author}'

    def book_cover(self):
        return mark_safe(f'<img> src="{self.cover}" width="100" height="100"/> ')


class UserFeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    feedback = models.TextField(verbose_name='Введите отзыв о книге', null=True, blank=True)

    def __str__(self):
        return f'Отзыв пользователя - {self.user}'

# Create your models here.
