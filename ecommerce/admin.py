from django.contrib import admin
from .models import Article, CheckOut, ArticleCart

# Register your models here.
admin.site.register(Article)
admin.site.register(CheckOut)
admin.site.register(ArticleCart)
