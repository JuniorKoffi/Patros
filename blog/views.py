from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Categorie, Tag, Author, \
     Article, Commentaire, Avis
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer



# Create your views here.
@api_view(['GET'])
def allArticles(request):
    articles = Article.objects.all()
    serialisation = ArticleSerializer(articles, many= True)
    return Response(serialisation.data)

@api_view(['GET'])
def getArticle(request,id):
    article = Article.object.get(id=id)
    serialisation = ArticleSerializer(article)
    return Response(serialisation.data)

@api_view(['GET'])
def getArticle(request, id):
    article = Article.objects.get(id=id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
#--------------------------------
@api_view(['POST'])
def addArticle(request):
    serializer = ArticleSerializer(data = request.data, many= True)
    if serializer.is_valid:
        serializer.save()
    return Response(serializer.data)
#--------------------------------
@api_view(['PUT'])
def updateArticle(request, id):
    article = Article.objects.get(id=id)
    serializer = ArticleSerializer(instance= article, data = request.data, many= True)
    if serializer.is_valid:
        serializer.save()
    return Response(serializer.data)

def blog(request):
    articles = Article.objects.filter(status=True)
    datas = {
        'articles': articles
    }
    return render(request, 'pages/blog.html', datas)




def blog_details(request, pk):
    article = Article.objects.get(id=pk)
    if request.POST:
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        comment = request.POST.get('comment', '')
        commentaire = Commentaire()
        commentaire.nom = name
        commentaire.article = article
        commentaire.email = email
        commentaire.commentaire = comment
        commentaire.save()

    datas = {
        'article': article
    }
    return render(request, 'pages/blog-single.html', datas)


def avis(request, pk, choice):
    article = Article.objects.get(id=pk)
    if choice == 'like':
        avi = Avis()
        avi.user = request.user
        avi.article = article
        avi.like = True 
        avi.save()
    elif choice == 'dislike':
        avi = Avis()
        avi.user = request.user
        avi.article = article
        avi.like = False 
        avi.save()
    return redirect('blog_detail', pk=article.id)