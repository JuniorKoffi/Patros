from django.shortcuts import render, redirect
from django.core.mail import send_mail

from . import models
from .models import Contact
from .models import About, Service, Lblog, Team, Portfolio, Localisation

# Create your views here.
def Accueil(request):
    about = About.objects.filter()
    services = Service.objects.filter()
    lblogs = Lblog.objects.filter()
    teams = Team.objects.filter()
    portfolios = Portfolio.objects.filter()
    localisations = Localisation.objects.filter()




    if request.method == 'POST':
        contact = models.Contact()
        nom = request.POST.get('first_name')
        email = request.POST.get('email')
        contenu = request.POST.get('message')

        contact.nom = nom
        contact.email = email
        contact.contenus = contenu
        contact.save()


    datas = {

        'about': about,
        'services': services,
        'lblogs': lblogs,
        'teams': teams,
        'portfolios': portfolios,
        'localisations': localisations,


    }

    return render(request, "Accueil.html", datas)









