from django.contrib import admin
from django.urls import path
from . import views, views_landing
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    # Pagina principal con tabla general ----------------------------------------------------------->
    path("inicio/", login_required(permission_required('seguridadVial.view_elementos')(views.paginaPrincipal)), name="paginaPrincipal"),
                  
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
    path("instituciones/", login_required(permission_required('seguridadVial.view_institucion')(views.ListaInstitucion.as_view())), name="listaInstituciones"),
    path("instituciones/detalle/<str:pk>", login_required(permission_required('seguridadVial.view_institucion')(views.institucionDetalle)), name="institucionDetalle"),
    path("instituciones/nueva", login_required(permission_required('seguridadVial.add_institucion')(views.InstitucionNueva.as_view())), name="nuevaInstitucion"),
    path("instituciones/modificar/<str:pk>", login_required(permission_required('seguridadVial.change_institucion')(views.InstitucionModificar.as_view())), name="modificarInstitucion"),
    path("instituciones/borrar/<str:pk>", login_required(permission_required('seguridadVial.delete_institucion')(views.InstitucionBorrar.as_view())), name="borrarInstitucion"),

    
    # UlRs [Landing Page] 
    
    # Public
    path("", views_landing.ActiveCatastropheListView, name="home"), # esta 
    path("detalleCatastrofe/<int:pk>/", views_landing.DetalleCatastrofe, name="detalleCatastrofe"), # esta 

    # Admin  login_required(permission_required('miAplicacion.add_orden')(views.ordenNuevo)), name="ordenNueva"),
    path("listaDesastre/", login_required(permission_required('defensaCivil.add_catastrophe')(views_landing.DashboardCatastrophe)), name="Lista-Desastre"),
    path("activar/<int:pk>/", login_required(permission_required('defensaCivil.add_catastrophe')(views_landing.ActiveDisaster)), name="Activar"),
    path("crear/", login_required(permission_required('defensaCivil.add_catastrophe')(views_landing.CatastropheCreateView.as_view())), name="crear"),
    path("modificar/<int:pk>/", login_required(permission_required('defensaCivil.add_catastrophe')(views_landing.CatastropheUpdateView.as_view())), name="Modificar"),
    path("Eliminar/<int:pk>/", login_required(permission_required('defensaCivil.add_catastrophe')(views_landing.DeleteDisaster.as_view())), name="Eliminar"),

    # Pdf frameMap
    path('crear/frame/', login_required(permission_required('defensaCivil.add_PdfFrame')(views_landing.PdfFrameCreateView.as_view())), name='pdf_create'),
    path('editar/<int:pk>/', login_required(permission_required('defensaCivil.add_PdfFrame')(views_landing.PdfFrameUpdateView.as_view())), name='pdf_update'),
    path('eliminar/<int:pk>/', login_required(permission_required('defensaCivil.add_PdfFrame')(views_landing.PdfFrameDeleteView.as_view())), name='pdf_delete'),

    # SubForm
    path('crear-subcatastrofe/', login_required(views_landing.SubCatastrofeCreateView.as_view()), name='subcar_crear'),

    path('editar-subcatastrofe/<int:pk>/', login_required(views_landing.SubCatastrofeUpdateView.as_view()), name='subcat_update'),
    
    path('delete-subcatastrofe/<int:pk>/', login_required(views_landing.SubCatastrofeDeleteView.as_view()), name='subcat_delete'),







    
    
    # new features
    
    
]