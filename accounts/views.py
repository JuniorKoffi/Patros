from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from . tokens import generateToken


# Create your views here.
def Register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpwd = request.POST['comfirmpwd']


    return render(request, 'register.html')

def Login(request):

   datas = {}

   return render(request, 'login.html', datas)


def Logout(request):

    datas = {}

    return render(request, 'logout.html', datas)

