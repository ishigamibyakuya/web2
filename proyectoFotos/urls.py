"""proyectoFotos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import authenticate, login
from principal import views as views_principal
from backend import views as views_backend
from django.contrib.auth import views as auth_views
import backend 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views_principal.logout_view, name="logout"),
    path('', views_principal.iniciarSesion, name=('iniciar')),
    path('nuevoUsuario', views_principal.formulario_crear_usuario),
    path('crearUsuario/', views_principal.crear_usuario),
    path('index', views_principal.Principal,name=('index')),
    path('verFoto/<int:id>', views_principal.verFoto),
    path('adminFotos/', views_backend.IngresoFotos), 
    path('GuardarFoto/', views_backend.GuardarFoto),
    path('<int:idFoto>/actualizar/', views_principal.editar_pregunta), 
    path('editar/', views_principal.actualizar_pregunta),
    path('<int:idFoto>/eliminar/', views_principal.eliminar_cliente), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("login/", views_principal.login, name="login"),
    
]
 

