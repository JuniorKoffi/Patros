from django.contrib import admin
from .models import Categorie, Tag, Author, \
     Article, Commentaire, Avis
# Register your models here.

admin.site.register(Categorie)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Commentaire)
admin.site.register(Avis)