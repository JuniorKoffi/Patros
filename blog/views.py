from django.shortcuts import render, redirect
from .models import Categorie, Tag, Author, \
     Article, Commentaire, Avis


# Create your views here.
def index(request):
    datas = {

    }
    return render(request, 'pages/index.html', datas)


def blog(request):
    articles = Article.objects.filter(status=True)
    datas = {
        'articles': articles
    }
    return render(request, 'pages/blog.html', datas)


def contact(request):
    datas = {

    }
    return render(request, 'pages/contact.html', datas)


def about(request):
    datas = {

    }
    return render(request, 'pages/portfolio.html', datas)


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