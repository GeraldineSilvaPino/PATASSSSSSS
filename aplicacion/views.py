from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import CrearCuentaForm, ProductoForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required
from .models import Compra, CompraItem, Producto
import json
# Create your views here.
@login_required
@csrf_exempt
def guardar_compra(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart = data.get('cart', [])
            total = sum(item['price'] * item['quantity'] for item in cart)
            
            if not cart:
                return JsonResponse({'mensaje': 'El carrito está vacío o no es válido'}, status=400)

            compra = Compra.objects.create(user=request.user, total=total)

            for item in cart:
                CompraItem.objects.create(
                    compra=compra,
                    producto_name=item['name'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            return JsonResponse({'mensaje': 'Compra guardada exitosamente'}, status=200)
        except Exception as e:
            return JsonResponse({'mensaje': f'Error al guardar la compra: {str(e)}'}, status=500)

    return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
def menu(request):
    return render(request, "aplicacion/menu.html")
@login_required
@permission_required('aplicacion.add_permission')
def adVentas(request):
    return render(request, 'aplicacion/adVentas.html')
@login_required
@permission_required('aplicacion.add_permission')
def adUsuario(request):
    usuarios_admin = User.objects.filter(is_staff=True)

    if request.method == 'POST':
        # Agregar usuario administrador
        if 'agregar_usuario' in request.POST:
            nombre_usuario = request.POST.get('nombre_usuario')
            nombre = request.POST.get('nombre')
            contrasena = request.POST.get('contrasena')

            if User.objects.filter(username=nombre_usuario).exists():
                mensaje_error = f'El nombre de usuario "{nombre_usuario}" ya está registrado.'
                return render(request, 'aplicacion/adUsuario.html', {'usuarios_admin': usuarios_admin, 'error': mensaje_error})

            user = User.objects.create_user(username=nombre_usuario, password=contrasena)
            user.first_name = nombre
            user.is_staff = True
            user.save()

            mensaje_exito = f'Se ha agregado el usuario administrador "{nombre_usuario}" correctamente.'
            return render(request, 'aplicacion/adUsuario.html', {'usuarios_admin': usuarios_admin, 'exito': mensaje_exito})

        # Editar usuario administrador
        elif 'editar_usuario' in request.POST:
            usuario_id = request.POST.get('usuario_id')
            nuevo_nombre = request.POST.get('nuevo_nombre')

            try:
                user = User.objects.get(id=usuario_id)
                user.first_name = nuevo_nombre
                user.save()

                mensaje_exito = f'Se ha editado el usuario administrador "{user.username}" correctamente.'
                return render(request, 'aplicacion/adUsuario.html', {'usuarios_admin': usuarios_admin, 'exito': mensaje_exito})

            except User.DoesNotExist:
                mensaje_error = 'El usuario administrador que intentas editar no existe.'
                return render(request, 'aplicacion/adUsuario.html', {'usuarios_admin': usuarios_admin, 'error': mensaje_error})

        # Eliminar usuario administrador
        elif 'eliminar_usuario' in request.POST:
            usuario_id = request.POST.get('usuario_id')

            try:
                user = User.objects.get(id=usuario_id)
                user.delete()

                mensaje_exito = f'Se ha eliminado el usuario administrador "{user.username}" correctamente.'
                return render(request, 'aplicacion/adUsuario.html', {'usuarios_admin': usuarios_admin, 'exito': mensaje_exito})

            except User.DoesNotExist:
                mensaje_error = 'El usuario administrador que intentas eliminar no existe.'
                return render(request, 'aplicacion/adUsuario.html', {'usuarios_admin': usuarios_admin, 'error': mensaje_error})

    return render(request, 'aplicacion/adUsuario.html', {'usuarios_admin': usuarios_admin})
def carlsjr(request):
    return render(request, "aplicacion/carlsjr.html")
@login_required
@permission_required('aplicacion.add_permission')
def adPedidos(requets):
    compras = Compra.objects.all()
    return render(requets, 'aplicacion/adPedidos.html', {'compras': compras})

def salir(request):
    logout(request)
    return redirect(to = 'menu')
def crearcuenta(request):
    form=CrearCuentaForm()
    datos={
        "form":form
    }
    if request.method=="POST":
        form=CrearCuentaForm(data=request.POST)
        usr=request.POST["username"]
        existe=User.objects.filter(username=usr).exists()
        if existe:
            alerta="El usuario ya existe"
            datos={
                "form":form,
                "alerta":alerta
            }
        else:
            if form.is_valid():
                form.save()
                return redirect(to="login")
            datos={
                "form":form
            }
    return render(request, "registration/crearcuenta.html", datos)
@login_required
def carro(request):
    productos = Producto.objects.all()
    return render(request, "aplicacion/carro.html", {'productos': productos})
def choclo(request):
    return render(request, "aplicacion/choclo.html")
def coronta(request):
    return render(request, "aplicacion/coronta.html")
def cotonito(request):
    return render(request, "aplicacion/cotonito.html")
def cuarto(request):
    return render(request, "aplicacion/cuarto.html")
def datosperson(request):
    return render(request, "aplicacion/datosperson.html")
def duna(request):
    return render(request, "aplicacion/duna.html")
def factura(request):
    return render(request, "aplicacion/factura.html")
def formulario(request):
    return render(request, "aplicacion/formulario.html")
def quinto(request):
    return render(request, "aplicacion/quinto.html")
def robin(request):
    return render(request, "aplicacion/robin.html")
@login_required
def segundo(request):
    return render(request, "aplicacion/segundo.html")
def tarjeta(request):
    return render(request, "aplicacion/tarjeta.html")
def tercero(request):
    return render(request, "aplicacion/tercero.html")
@login_required
@permission_required('aplicacion.add_permission')
def darchar(requets):
    usuarios=User.objects.all()
    datos={
        "usuarios":usuarios
    }
    return render(requets, 'aplicacion/adPedidos.html', datos)

def adProductos(request):
    producto = Producto.objects.all()
    return render(request, "aplicacion/adProductos.html", {'producto': producto})

def agregarproducto(request):
    if request.method == 'POST':    
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirige a la página adProductos después de agregar el producto
            return redirect('adProductos')
    else:
        form = ProductoForm()
    
    return render(request, "aplicacion/agregarproducto.html", {'form': form})   
def eliminarproducto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        # Si se confirma la eliminación, se elimina el producto
        producto.delete()
        return redirect('adProductos')  # Redirige a la página principal de administración

    return render(request, 'aplicacion/eliminarproducto.html', {'producto': producto}) 
def editarproducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('adProductos')  # Redirige a la página principal de administración
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'aplicacion/editarproducto.html', {'form': form, 'producto': producto})