from django.urls import path, include
from . import views

app_name = 'ecommerce'


urlpatterns = [
    path('', views.index, name='indexz'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:id>', views.product, name='product'),
    path('categorie/', views.categorie, name='categorie'),

    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('delete-article/<int:id>/', views.delete_article, name='delete_article'),

]
