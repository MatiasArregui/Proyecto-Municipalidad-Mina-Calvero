from django.contrib import admin
from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth.views import LoginView
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    # Login ----------------------------------------------------------------------------------->
    path('', LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=LoginForm
    ), name='login'),
    
    # Personas URLs--------------------------------------------------------------------------------->
    path("personas/", login_required(views.listaPersona.as_view()), name="listaPersonas"),
    path("personas/nuevaPersona", login_required(views.PersonaNueva.as_view()), name="nuevaPersona"),
    path("personas/modificarPersona/<str:pk>", login_required(views.PersonaModificar.as_view()), name="modificarPersona"),
    path("personas/borrarPersona/<str:pk>", login_required(views.PersonaBorrar.as_view()), name="borrarPersona"),
    
    # Personas URLs--------------------------------------------------------------------------------->
    path("elementos/", login_required(views.listaElemento.as_view()), name="listaElementos"),
    path("elementos/nuevoElemento", login_required(views.ElementoNuevo.as_view()), name="nuevoElemento"),
    path("elementos/modificarElemento/<str:pk>", login_required(views.ElementoModificar.as_view()), name="modificarElemento"),
    path("elementos/borrarElemento/<str:pk>", login_required(views.ElementoBorrar.as_view()), name="borrarElemento"),
    
    # Personas URLs--------------------------------------------------------------------------------->
    path("categorias/", login_required(views.listaCategoria.as_view()), name="listaCategorias"),
    path("categorias/nuevaCategoria", login_required(views.CategoriaNueva.as_view()), name="nuevaCategoria"),
    path("categorias/modificarCategoria/<str:pk>", login_required(views.CategoriaModificar.as_view()), name="modificarCategoria"),
    path("categorias/borrarCategoria/<str:pk>", login_required(views.CategoriaBorrar.as_view()), name="borrarCategoria"),
    
    # Personas URLs--------------------------------------------------------------------------------->
    path("cargos/", login_required(views.listaCargos.as_view()), name="listaCargos"),
    path("cargos/nuevoCargo", login_required(views.CargoNuevo.as_view()), name="nuevoCargo"),
    path("cargos/modificarCargo/<str:pk>", login_required(views.CargoModificar.as_view()), name="modificarCargo"),
    path("cargos/borrarCargo/<str:pk>", login_required(views.CargoBorrar.as_view()), name="borrarCargo"),
]