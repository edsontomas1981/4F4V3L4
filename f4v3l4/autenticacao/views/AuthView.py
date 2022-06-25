from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from usuario.models import Usuarios
from f4v3l4.forms.AuthForm import RecoveryForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import hashlib

def recovery_view(request):
    recoveryForm = RecoveryForm()
    message = None
    if request.method == 'POST':
        recoveryForm = RecoveryForm(request.POST)
    if recoveryForm.is_valid():
        email = request.POST['email']
    return render(request, template_name='auth/auth.html', status=200)

