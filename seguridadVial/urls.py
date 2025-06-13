from django.contrib import admin
from django.urls import path
from . import views
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required, permission_required

from .views import landing_page

urlpatterns = [


    # Pagina principal con tabla general ----------------------------------------------------------->
    path("inicio/", login_required(permission_required('seguridadVial.view_elementos')(views.paginaPrincipal)), name="paginaPrincipal"),
                    #   login_required(permission_required('miAplicacion.view_cliente')(views.listaClientes.as_view())),
                    # add_cargo
                    # change_cargo
                    # delete_cargo
                    # view_cargo
    # Personas URLs--------------------------------------------------------------------------------->
    path("personas/", login_required(permission_required('seguridadVial.view_persona')(views.listaPersona.as_view())), name="listaPersonas"),
    path("personas/nuevaPersona", login_required(permission_required('seguridadVial.add_persona')(views.PersonaNueva.as_view())), name="nuevaPersona"),
    path("personas/modificarPersona/<str:pk>", login_required(permission_required('seguridadVial.change_persona')(views.PersonaModificar.as_view())), name="modificarPersona"),
    path("personas/borrarPersona/<str:pk>", login_required(permission_required('seguridadVial.delete_persona')(views.PersonaBorrar.as_view())), name="borrarPersona"),
    
    # Personas URLs--------------------------------------------------------------------------------->
    path("elementos/", login_required(permission_required('seguridadVial.view_elementos')(views.listaElemento.as_view())), name="listaElementos"),
    path("elementos/nuevoElemento", login_required(permission_required('seguridadVial.add_elementos')(views.ElementoNuevo.as_view())), name="nuevoElemento"),
    path("elementos/modificarElemento/<str:pk>", login_required(permission_required('seguridadVial.change_elementos')(views.ElementoModificar.as_view())), name="modificarElemento"),
    path("elementos/borrarElemento/<str:pk>", login_required(permission_required('seguridadVial.delete_elementos')(views.ElementoBorrar.as_view())), name="borrarElemento"),
    
    # Personas URLs--------------------------------------------------------------------------------->
    path("categorias/", login_required(permission_required('seguridadVial.view_categoria')(views.listaCategoria.as_view())), name="listaCategorias"),
    path("categorias/nuevaCategoria", login_required(permission_required('seguridadVial.add_categoria')(views.CategoriaNueva.as_view())), name="nuevaCategoria"),
    path("categorias/modificarCategoria/<str:pk>", login_required(permission_required('seguridadVial.change_categoria')(views.CategoriaModificar.as_view())), name="modificarCategoria"),
    path("categorias/borrarCategoria/<str:pk>", login_required(permission_required('seguridadVial.delete_categoria')(views.CategoriaBorrar.as_view())), name="borrarCategoria"),
    
    # Personas URLs--------------------------------------------------------------------------------->
    path("cargos/", login_required(permission_required('seguridadVial.view_cargo')(views.listaCargos.as_view())), name="listaCargos"),
    path("cargos/nuevoCargo", login_required(permission_required('seguridadVial.add_cargo')(views.CargoNuevo.as_view())), name="nuevoCargo"),
    path("cargos/modificarCargo/<str:pk>", login_required(permission_required('seguridadVial.change_cargo')(views.CargoModificar.as_view())), name="modificarCargo"),
    path("cargos/borrarCargo/<str:pk>", login_required(permission_required('seguridadVial.delete_cargo')(views.CargoBorrar.as_view())), name="borrarCargo"),
   
    # Personas URLs--------------------------------------------------------------------------------->
    path("instituciones/", login_required(permission_required('seguridadVial.view_institucion')(views.ListaInstitucion.as_view())), name="listaInstituciones"),
    path("instituciones/nueva", login_required(permission_required('seguridadVial.add_institucion')(views.InstitucionNueva.as_view())), name="nuevaInstitucion"),
    path("instituciones/modificar/<str:pk>", login_required(permission_required('seguridadVial.change_institucion')(views.InstitucionModificar.as_view())), name="modificarInstitucion"),
    path("instituciones/borrar/<str:pk>", login_required(permission_required('seguridadVial.delete_institucion')(views.InstitucionBorrar.as_view())), name="borrarInstitucion"),

    
    
    
    # URLs QUE VAN A PERTENECER A LA LANDING PAGE
    # estructura basica de una url: 
    # path("nombreDelLink", modulo.funcionQueAccedemos, name="nombreDeLaUrl")
    # recuerden que el punto es lo que nos permite acceder a lo que compone la clase (metodos o atributos) y el name= es donde le damos un nombre a la Urls para usarlas en el template.ej:
    # href="{% url "listaPersonas" %}" url es una palabra reservada de django que nos indica que debemos llamar a la Url: listaPersonas
    # path("home/", views.paginaPrincipal, name="paginaPrincipal"),
    # definan la url que conecta a su parte del proyecto.

    #aca agrego la leading page como inicio
    path('', landing_page, name='landing_page'),
    
]