from django.contrib import admin

# Register your models here.

from .models import Pregunta, Eleccion

# Registra los modelos dentro del admin
admin.site.register(Pregunta)
admin.site.register(Eleccion)
