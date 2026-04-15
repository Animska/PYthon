from django.shortcuts import render, redirect
from .forms import RegistroForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

#VISTA INDICE
def index(request):
    '''
    Retorna el html index
    '''
    return render(request, 'shop/index.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'shop/registro.html', {'form' : form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def iniciar_sesion(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            error_message = "Usuario o contaseña incorrecta."
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {
        'form': form,
        'error_messages': error_message
    })

@login_required
def perfil(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('perfil')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'shop/perfil.html', {
        'u_form': u_form,
        'p_form': p_form
    })