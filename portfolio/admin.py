from django.contrib import admin
from .models import Author, Article, Post

# Register your models here.

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Article)
