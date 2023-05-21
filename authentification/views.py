from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.shortcuts import redirect, render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .tokens import generateToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'authentificati/password_reset.html'
    email_template_name = 'authentificati/password_reset_email.html'
    subject_template_name = 'authentificati/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('ecommerce:index')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpwd = request.POST.get('comfirmpwd')
        if User.objects.filter(username=username):
            messages.error(request, 'username already taken please try another.')
            return redirect('authentification:signup')
        if User.objects.filter(email=email):
            messages.error(request, 'This email has an account.')
            return redirect('authentification:signup')
        if len(username) > 10:
            messages.error(request, 'Please the username must not be more than 10 character.')
            return redirect('authentification:signup')
        if len(username) < 5:
            messages.error(request, 'Please the username must be at leat 5 characters.')
            return redirect('authentification:signup')
        if not username.isalnum():
            messages.error(request, 'username must be alphanumeric')
            return redirect('authentification:signup')

        if password != confirmpwd:
            messages.error(request, 'The password did not match! ')
            return redirect('authentification:signup')

        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = firstname
        my_user.last_name = lastname
        my_user.is_active = False
        my_user.save()
        messages.success(request,
                         'Your account has been successfully created. we have sent you an email You must comfirm in order to activate your account.')
        # send email when account has been created successfully
        subject = "Welcome to Tale"
        message = "Welcome " + my_user.first_name + " " + my_user.last_name + "\n thank for chosing Tale.\n To order login you need to comfirm your email account.\n thanks\n\n\nSincerly,\n\n\nTALE"

        from_email = settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)

        # send the the confirmation email
        current_site = get_current_site(request)
        email_suject = "confirm your email Tale Login!"
        messageConfirm = render_to_string("emailConfimation.html", {
            'name': my_user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': generateToken.make_token(my_user),
        })

        email = EmailMessage(
            email_suject,
            messageConfirm,
            settings.EMAIL_HOST_USER,
            [my_user.email]
        )

        email.fail_silently = False
        email.send()
        return redirect('authentification:signin')
    return render(request, 'authentificati/signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        my_user = User.objects.get(username=username)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            return redirect('ecommerce:indexz')
        elif my_user.is_active == False:
            messages.error(request, 'you have not confirm your  email do it, in order to activate your account')
            return redirect('authentification:signin')
        else:
            messages.error(request, 'bad authentification')
            return redirect('authentification:signin')



    return render(request, 'authentificati/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'logout successfully!')
    return redirect('ecommerce:indexz')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None

    if my_user is not None and generateToken.check_token(my_user, token):
        my_user.is_active = True
        my_user.save()
        messages.success(request, "You are account is activated you can login by filling the form below.")
        return redirect("authentification:signin")
    else:
        messages.success(request, 'Activation failed please try again')
        return redirect('home')


