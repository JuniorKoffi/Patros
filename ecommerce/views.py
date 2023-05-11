from .models import Article, ArticleCart
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django import template

# Create your views here.


def index(request):
    articles = Article.objects.filter(status=True)
    datas = {
        'articles': articles,
    }
    return render(request, 'ecom/index.html', datas)


def categorie(request):
    return render(request, 'ecom/categorie.html')


@login_required
def cart(request):
    articles = ArticleCart.objects.filter(user=request.user)
    total_price = sum(item.article.prix * item.quantity for item in articles)
    datas = {
        'articles': articles,
        'total_price': total_price
    }

    return render(request, 'ecom/cart.html', datas)


def checkout(request):
    return render(request, 'ecom/checkout.html')


def product(request, id):
    article = Article.objects.get(id=id)
    datas = {
        'article': article,
    }
    return render(request, 'ecom/product.html', datas)


@login_required
def add_to_cart(request, id):
    article = get_object_or_404(Article, id=id)
    quantity = request.POST.get('quantity', 1)

    artic, created = ArticleCart.objects.get_or_create(
        article=article,
        defaults={'quantity': quantity},
        user=request.user,
    )

    if not created:
        artic.quantity += int(quantity)
    return redirect('ecommerce:indexz')


@login_required
def clear_cart(request):
    ArticleCart.objects.filter(user=request.user).delete()
    return redirect('ecommerce:cart')


@login_required
def update_cart(request):
    if request.method == 'POST':
        cart_items = request.POST.getlist('cart_item')
        quantities = request.POST.getlist('quantity')
        for item_id, quantity in zip(cart_items, quantities):
            cart_item = get_object_or_404(ArticleCart, id=item_id)
            cart_item.quantity = int(quantity)
            cart_item.save()
    return redirect('ecommerce:cart')


@login_required
def delete_article(request, id):
    ArticleCart.objects.filter(user=request.user, id=id).delete()
    return redirect('ecommerce:cart')
