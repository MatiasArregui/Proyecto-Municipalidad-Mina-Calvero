from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from .models import Cargo, Categoria, Elementos, Institucion, InstitucionPersona, Persona
from .forms import PersonaForm, CargoForm, CategoriaForm, AuthenticationForm, InstitucionForm, InstitucionPersonaForm, InstitucionPersonaFormSet, ElementosForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.db.models import ProtectedError
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
import os


# Persona Views ------------------------------------------------------------------------------>
    #Ver Personas
class listaPersona(ListView):
    model = Persona
    template_name = os.path.join("defensaCivil", "listas", "listaPersonas.html")
    context_object_name = 'personas'
    paginate_by = 7
    #Crear persona
class PersonaNueva(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = os.path.join("defensaCivil", "formularios", "personaForm.html")
    success_url = reverse_lazy('listaPersonas')
    #Modificar persona
class PersonaModificar(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = os.path.join("defensaCivil", "formularios", "personaForm.html")
    success_url = reverse_lazy('listaPersonas')
    #Borrar persona
class PersonaBorrar(DeleteView):
    model = Persona
    template_name = os.path.join("defensaCivil", "confirmacionBorrado", "personaBorrar.html")
    success_url = reverse_lazy('listaPersonas')
    
# Elemento Views ------------------------------------------------------------------------------>
    #Ver Elementos
class listaElemento(ListView):
    model = Elementos
    template_name = os.path.join("defensaCivil", "listas", "listaElementos.html")
    context_object_name = 'elementos'
    paginate_by = 7
    #Crear elemento
class ElementoNuevo(CreateView):
    model = Elementos
    form_class = ElementosForm
    template_name = os.path.join("defensaCivil", "formularios", "elementoForm.html")
    success_url = reverse_lazy('listaElementos')
    #Modificar Elemento
class ElementoModificar(UpdateView):
    model = Elementos
    form_class = ElementosForm
    template_name = os.path.join("defensaCivil", "formularios", "elementoForm.html")
    success_url = reverse_lazy('listaElementos')
    #Borrar Elemento
class ElementoBorrar(DeleteView):
    model = Elementos
    template_name = os.path.join("defensaCivil", "confirmacionBorrado", "elementoBorrar.html")
    success_url = reverse_lazy('listaElementos')

# Categoria Views ------------------------------------------------------------------------------>
    #Ver categorias
class listaCategoria(ListView):
    model = Categoria
    template_name = os.path.join("defensaCivil", "listas", "listaCategorias.html")
    context_object_name = 'categorias'
    paginate_by = 7
    #Crear categoria
class CategoriaNueva(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = os.path.join("defensaCivil", "formularios", "categoriaForm.html")
    success_url = reverse_lazy('listaCategorias')
    #Modificar categoria
class CategoriaModificar(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = os.path.join("defensaCivil", "formularios", "categoriaForm.html")
    success_url = reverse_lazy('listaCategorias')
    #Borrar categoria
class CategoriaBorrar(DeleteView):
    model = Categoria
    template_name = os.path.join("defensaCivil", "confirmacionBorrado", "categoriaBorrar.html")
    success_url = reverse_lazy('listaCategorias')

# Categoria Views ------------------------------------------------------------------------------>
    #Ver categorias
class listaCargos(ListView):
    model = Cargo
    template_name = os.path.join("defensaCivil", "listas", "listaCargos.html")
    context_object_name = 'cargos'
    paginate_by = 7
    #Crear categoria
class CargoNuevo(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = os.path.join("defensaCivil", "formularios", "cargoForm.html")
    success_url = reverse_lazy('listaCargos')
    #Modificar categoria
class CargoModificar(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = os.path.join("defensaCivil", "formularios", "cargoForm.html")
    success_url = reverse_lazy('listaCargos')
    #Borrar categoria
class CargoBorrar(DeleteView):
    model = Cargo
    template_name = os.path.join("defensaCivil", "confirmacionBorrado", "cargoBorrar.html")
    success_url = reverse_lazy('listaCargos')



# Instituciones Views ------------------------------------------------------------------------------>
    #Ver instituciones
class ListaInstitucion(ListView):
    model = Institucion
    template_name = os.path.join("defensaCivil", "listas", "listaInstituciones.html")
    context_object_name = 'instituciones'

    #Crear instituciones
class InstitucionNueva(CreateView):
    model = Institucion
    form_class = InstitucionForm
    template_name = os.path.join("defensaCivil", "formularios", "institucionForm.html")
    success_url = reverse_lazy('listaInstituciones')

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = InstitucionPersonaFormSet()
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = InstitucionPersonaFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    #Modificar instituciones
class InstitucionModificar(UpdateView):
    model = Institucion
    form_class = InstitucionForm
    template_name = os.path.join("defensaCivil", "formularios", "institucionForm.html")
    success_url = reverse_lazy('listaInstituciones')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = InstitucionPersonaFormSet(instance=self.object)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = InstitucionPersonaFormSet(request.POST, instance=self.object)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(self.success_url)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    #Borrar instituciones
class InstitucionBorrar(DeleteView):
    model = Institucion
    template_name = os.path.join("defensaCivil", "confirmacionBorrado", "institucionBorrar.html")
    success_url = reverse_lazy('listaInstituciones')
        