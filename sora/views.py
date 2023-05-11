from django.shortcuts import render, redirect
from django.core.mail import send_mail

from . import models
from .models import Contact

# Create your views here.
def Accueil(request):
    if request.method == 'POST':
        contact = models.Contact()
        nom = request.POST.get('first_name')
        email = request.POST.get('email')
        contenu = request.POST.get('message')

        contact.nom = nom
        contact.email = email
        contact.contenus = contenu
        contact.save()


    datas = {}

    return render(request, "Accueil.html", datas)









