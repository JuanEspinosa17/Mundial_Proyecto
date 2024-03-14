from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import equipo  # Importa el modelo 'equipo'
from django.shortcuts import get_object_or_404
from .models import jugador, tecnico


def index(request):
    return render(request, 'index.html', {
        # context
    })

def base_pais(request):
    return render(request, 'layouts/base_pais.html', {
        # context
    })

@login_required
def equipos(request):
    equipos = equipo.objects.all()  # Usamos 'equipo' en singular
    return render(request, 'equipos/equipos.html', {'equipos': equipos})

def login_administrador(request):
    return render(request, 'login_administrador.html', {
        # context
    })

@login_required
def login(request):
    return render(request, 'login.html', {
        # context
    })

def logout(request):
    auth_logout(request)
    return redirect('index')

from django.contrib import messages

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            # Autenticar al usuario después de registrarse
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                messages.success(request, '¡Registro exitoso! Te has autenticado correctamente.')
                return redirect('index')
            else:
                messages.error(request, '¡Ha ocurrido un error al intentar autenticarte después del registro!')
        else:
            messages.error(request, '¡El formulario de registro es inválido! Por favor, corrija los errores.')
    
    return render(request, 'registration/register.html', data)



def detalle_equipo(request, nombre_equipo):
    equipo_objeto = get_object_or_404(equipo, nombre=nombre_equipo)
    titulares = jugador.objects.filter(idestado__estado="Titular", idequipo=equipo_objeto)
    suplentes = jugador.objects.filter(idestado__estado="Suplente", idequipo=equipo_objeto)
    tecnicos = tecnico.objects.filter(idequipo=equipo_objeto)
    return render(request, 'equipos/equipo.html', {'equipo': equipo_objeto, "titulares": titulares, "suplentes": suplentes, "tecnicos": tecnicos})
