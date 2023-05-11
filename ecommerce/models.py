from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from PIL import Image
import os

def get_upload_path(instance, filename):
    return os.path.join('articleImage', str(instance.id), filename)

class Article(models.Model):
    name = models.CharField(max_length=40)
    prix = models.IntegerField(default=0)
    image1 = models.ImageField(upload_to=get_upload_path)
    image2 = models.ImageField(upload_to=get_upload_path)
    image3 = models.ImageField(upload_to=get_upload_path)
    description = models.TextField()


    # standard
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ArticleCart(models.Model):
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ecommerce_articles')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='ecommerce_cart', blank=True, null=True)

    # standard
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class CheckOut(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    number = models.CharField(max_length=30)
    mail = models.EmailField()
    description = models.TextField()

    # standard
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName



