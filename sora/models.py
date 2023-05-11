from django.db import models

# Create your models here.

class About(models.Model):
    contenus = models.TextField()

    def __str__(self):
        return self.contenus

class Service(models.Model):
    titre = models.CharField(max_length= 150)
    contenus = models.TextField()

    def __str__(self):
        return self.titre

class Lblog(models.Model):
    image = models.ImageField()
    contenus = models.TextField()

    def __str__(self):
        return self.image.name

class Team(models.Model):
    nom = models.CharField(max_length= 150)
    fonction = models.CharField(max_length= 150)
    description = models.TextField()

    def __str__(self):
        return self.nom

class Portfolio(models.Model):
    images = models.ImageField()

    def __str__(self):
        return self.images.name

class Localisation(models.Model):
    localisation = models.CharField(max_length= 150)
    number = models.IntegerField()
    mail = models.EmailField()

class Contact(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    contenus = models.TextField()
    active= models.BooleanField(default=False)

    # standard
    statuts = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_add']

    def __str__(self):
        return 'Contact {} by {}'.format(self.contenus, self.nom)
