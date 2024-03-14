from django.contrib import admin
from .models import jugador, equipo, rol, nacionalidad, estado, tecnico

# Register your models here.

admin.site.register(jugador)
admin.site.register(equipo)
admin.site.register(rol)
admin.site.register(nacionalidad)
admin.site.register(estado)
admin.site.register(tecnico)