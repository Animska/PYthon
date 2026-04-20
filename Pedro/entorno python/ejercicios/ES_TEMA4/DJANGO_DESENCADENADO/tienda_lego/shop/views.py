from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import RegistroForm, UserUpdateForm, ProfileUpdateForm
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            messages.success(request, "¡Tu perfil ha sido actualizado con éxito!")
            return redirect('perfil')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'shop/perfil.html', {
        'u_form': u_form,
        'p_form': p_form
    })
def catalogo(request):
    # Obtener parámetros de filtrado
    categoria_id = request.GET.get('categoria')
    estado = request.GET.get('estado')
    min_precio = request.GET.get('min_precio')
    max_precio = request.GET.get('max_precio')
    orden = request.GET.get('orden', 'nombre')
    
    # Queryset base
    productos = Product.objects.all()
    
    # Aplicar filtros
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    if estado:
        productos = productos.filter(estado=estado)
    if min_precio:
        try:
            productos = productos.filter(precio__gte=min_precio)
        except (ValueError, TypeError):
            pass
    if max_precio:
        try:
            productos = productos.filter(precio__lte=max_precio)
        except (ValueError, TypeError):
            pass
        
    # Ordenación
    if orden == 'precio_asc':
        productos = productos.order_by('precio')
    elif orden == 'precio_desc':
        productos = productos.order_by('-precio')
    else:
        productos = productos.order_by('nombre')
        
    # Paginación (6 por página)
    paginator = Paginator(productos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Categorías para el filtro
    categorias = Category.objects.all()
    
    return render(request, 'shop/catalogo.html', {
        'page_obj': page_obj,
        'categorias': categorias,
        'estados': Product.ESTADO_CHOICES,
        'filtros': {
            'categoria': categoria_id,
            'estado': estado,
            'min_precio': min_precio,
            'max_precio': max_precio,
            'orden': orden
        }
    })

from django.shortcuts import get_object_or_404

def producto_detalle(request, pk):
    producto = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/producto_detalle.html', {
        'producto': producto
    })

from .forms import ProductForm

@login_required
def crear_producto(request):
    if request.method == 'POST' and request.user.profile.es_vendedor:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.vendedor = request.user
            producto.save()
            messages.success(request, f"¡El set '{producto.nombre}' ha sido añadido correctamente!")
            return redirect('catalogo')
        else:
            messages.error(request, "Hubo un error al crear el producto. Revisa los datos.")
            # Si hay error, redirigimos de vuelta para que el usuario pueda ver qué falló 
            # (Aunque al ser un modal, lo ideal sería manejarlo con AJAX, pero por ahora 
            # redirigiremos a una página simple o al catálogo con mensajes)
            return redirect('catalogo')
    return redirect('catalogo')
