from django.shortcuts import render
from . import models

# Create your views here.

def Home(request):
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

    return render(request, "home.html", datas)
