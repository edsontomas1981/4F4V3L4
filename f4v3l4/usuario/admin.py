from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import Usuarios

admin.site.register(Usuarios,auth_admin.UserAdmin)

# Register your models here.
