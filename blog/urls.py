"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import blog, \
    blog_details, avis, allArticles, getArticle, addArticle, updateArticle
from .import views

urlpatterns = [
    path('blog', blog, name='blog'),
    path('blog/<int:pk>/details', blog_details, name='blog_detail'),
    path('blog/<int:pk>/avis/<str:choice>', avis, name='avis'),

    path('articles/', allArticles, name='allArticles'),
    # pour voir l'article selection par l'id
    path('article/<int:id>/', getArticle, name='getArticle'),
    # pour ajouter un article a la base de donnée
    path('addArticle/', addArticle, name='addArticle'),
    # pour update un article par l'id
    path('updateArticle/', updateArticle, name='updateArticle'),

]
