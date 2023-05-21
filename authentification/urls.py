from django.urls import path
# from . import views
# from django.contrib.auth import  views as vs
from .views import ResetPasswordView, signup, signin, signout, activate

from django.contrib.auth import views as auth_views


app_name = 'authentification'

urlpatterns = [
    path('', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('activate/<uidb64>/<token>', activate, name='activate'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentificati/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authentificati/password_reset_complete.html'), name='password_reset_complete'),


]
