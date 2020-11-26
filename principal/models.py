from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria=models.AutoField(primary_key=True, verbose_name='ID Categoría')
    nombreCategoria=models.CharField(max_length=50, verbose_name='Nombre Categoría')

class Foto(models.Model):
    idFoto=models.AutoField(primary_key=True, verbose_name='ID Foto')
    texto=models.CharField(max_length=200, verbose_name='Texto Foto')
    fechaRegistro=models.DateTimeField(verbose_name='Fecha de registro')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
