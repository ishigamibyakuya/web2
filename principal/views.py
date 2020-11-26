from django.shortcuts import render
from . import models
from principal.models import Foto
from principal.models import Categoria
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

#def login(request):
 # return render(request, 'login.html')

#@login_required
#def home(request):
  #return render(request, 'home.html')


def Principal(request):
    imagenes=models.Foto.objects.all()
    datos={"fotos":imagenes}
    return render(request, 'index.html', datos)

def verFoto(request, id):
    imagen=models.Foto.objects.get(idFoto=id)
    datos={"foto":imagen}
    return render(request, 'verFoto.html', datos)

def eliminar_cliente(request, idFoto):
    if request.user.is_authenticated:
        obj=get_object_or_404(Foto, idFoto=idFoto)
        if request.method == 'POST':
            obj.delete()
            return redirect('index')
        context={
        "object":obj
        }
        
        return render(request, 'eliminar.html', context)
    else:
        return redirect('iniciar')


def editar_pregunta(request, idFoto):
    if request.user.is_authenticated:
        foto = Foto.objects.get(idFoto=idFoto)
        context = { "foto": foto }  
        return render(request, 'actualizar.html', context)
    else:
        return redirect('iniciar')

def actualizar_pregunta(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            idFoto=request.POST['idFoto']
            texto=request.POST['texto']
            fechaRegistro=request.POST['fechaRegistro']
            idcategoria=request.POST['categoria']
            cat=models.Categoria.objects.get(idCategoria=idcategoria)
            nuevaFoto=models.Foto(idFoto=idFoto, texto=texto, fechaRegistro=fechaRegistro, categoria=cat)
            nuevaFoto.save()
            return redirect('index')        
        else:
            return redirect('index')
    return redirect('iniciar')
    
def iniciarSesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
    
    context = {}
    return render(request, 'iniciarSesion.html', context)

def formulario_crear_usuario(request):
    context = { }
    return render(request, 'crearUsuario.html', context)


def crear_usuario(request):

    usuario = request.POST["txt_usuario"]
    email1 = request.POST["txt_email"]
    clave = request.POST["txt_clave"]
    user = User.objects.create_user(usuario, email1, clave)
    return redirect('iniciar')

def logout_view(request):
    logout(request)
    return redirect('iniciar')
