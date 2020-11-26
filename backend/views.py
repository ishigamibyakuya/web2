from django.shortcuts import render
from principal import models
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from principal.models import Foto
#importa el objeto que permite administrar el sistema de archivos
#es independiente del sistema operativo
from django.core.files.storage import FileSystemStorage

# Create your views here.
def IngresoFotos(request):
    categorias=models.Categoria.objects.all()

    datos={"categorias":categorias}
    return render(request, 'fotos.html', datos)

def GuardarFoto(request):
    if request.method=='POST':
        idFoto=request.POST['idFoto']
        texto=request.POST['texto']
        fechaRegistro=request.POST['fechaRegistro']
        idcategoria=request.POST['categoria']
        archImagen=request.FILES['archImagen']
        #Guardar el archivo en el disco
        fs=FileSystemStorage()
        nomImg=idFoto + '.jpg'
        fs.save(nomImg, archImagen)
        
        #Guardar los datos en la BD
        ##encontrar la categoria usando el idCategoría que viene desde el formulario
        cat=models.Categoria.objects.get(idCategoria=idcategoria)

        nuevaFoto=models.Foto(idFoto=idFoto, texto=texto, fechaRegistro=fechaRegistro, categoria=cat)

        nuevaFoto.save()
        return redirect('index')
        
    else:
        return HttpResponseRedirect('adminFotos/')
    



