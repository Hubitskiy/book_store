from .models import Book, UserFeedBack
from django.contrib import admin


class AdminUserFeedBack(admin.StackedInline):
    model = UserFeedBack


class AdminBook(admin.ModelAdmin):
    inlines = [AdminUserFeedBack]
    list_display = [
        'title',
        'author',
        'genre',
        'book_cover'
    ]


admin.site.register(Book, AdminBook)
# Register your models here.
