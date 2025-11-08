from django.contrib import admin
from .models import Nota

# Aca registramos los modelos que pueden ser accedidos mediante el panel administrativo de Django
admin.site.register(Nota)
