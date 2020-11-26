# Generated by Django 3.0.3 on 2020-10-15 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Categoría')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('idFoto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Foto')),
                ('texto', models.CharField(max_length=200, verbose_name='Texto Foto')),
                ('fechaRegistro', models.DateTimeField(verbose_name='Fecha de registro')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Categoria')),
            ],
        ),
    ]