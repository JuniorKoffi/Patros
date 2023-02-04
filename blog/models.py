from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
import datetime

User = get_user_model()

class Author (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="authors")
  
    # standards

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.user.username


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    #Standards
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.nom


class Tag (models.Model):
    nom =models.CharField(max_length=150)

    #Standards
    status= models.BooleanField(default=True)
    date_add= models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.nom


class Article(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='articles') # permet d'indiquer le fichier où recuperer les images
    contenu = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="articles")
    tag = models.ManyToManyField(Tag, related_name="articles_tag")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # Standards
    status= models.BooleanField(default=True)
    date_add= models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.titre


class Commentaire(models.Model):
    nom = models.CharField(max_length=150)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaire')
    email = models.EmailField()
    commentaire = models.TextField()

    # Standards
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.nom


class Avis(models.Model):
    like = models.BooleanField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='avis')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    # Standards
    status= models.BooleanField(default=True)
    date_add= models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.like