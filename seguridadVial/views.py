from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from .models import Cargo, Categoria, Elementos, Institucion, InstitucionPersona, InstitucionElemento, Persona
from .forms import PersonaForm, CargoForm, CategoriaForm, ElementosForm, AuthenticationForm, InstitucionForm, InstitucionPersonaForm, InstitucionPersonaFormSet, InstitucionElementoForm, InstitucionElementoFormSet
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.db.models import ProtectedError
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
import os


# Pagina principal ----------------------------------------------------------------------------------->
def paginaPrincipal(request):
    elementos = Elementos.objects.all()
    instituciones = Institucion.objects.all()
    personas = Persona.objects.all()
    # Combinar todos los conjuntos en una sola lista o QuerySet
    todo = list(elementos) + list(instituciones) + list(personas)
    context = {"todo": todo}
    return render(request, template_name= os.path.join("defensaCivil", "paginaPrincipal.html"), context=context)


# Persona Views ------------------------------------------------------------------------------>
    #Ver Personas
class listaPersona(ListView):
    model = Persona
    template_name = os.path.join("defensaCivil", "listas", "listaPersonas.html")
    context_object_name = 'personas'
    paginate_by = 7
    def get_queryset(self):
        # Ordenar alfabéticamente por el atributo 'nombre'
        return Persona.objects.all().order_by('nombre')
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

# Categoria Views ------------------------------------------------------------------------------>
    #Ver categorias
class listaCategoria(ListView):
    model = Categoria
    template_name = os.path.join("defensaCivil", "listas", "listaCategorias.html")
    context_object_name = 'categorias'
    paginate_by = 7
    def get_queryset(self):
        # Ordenar alfabéticamente por el atributo 'nombre'
        return Categoria.objects.all().order_by('nombre')
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

# Cargo Views ------------------------------------------------------------------------------>
    #Ver cargos
class listaCargos(ListView):
    model = Cargo
    template_name = os.path.join("defensaCivil", "listas", "listaCargos.html")
    context_object_name = 'cargos'
    paginate_by = 7
    def get_queryset(self):
        # Ordenar alfabéticamente por el atributo 'nombre'
        return Cargo.objects.all().order_by('nombre')
    #Crear cargos
class CargoNuevo(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = os.path.join("defensaCivil", "formularios", "cargoForm.html")
    success_url = reverse_lazy('listaCargos')
    #Modificar cargo
class CargoModificar(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = os.path.join("defensaCivil", "formularios", "cargoForm.html")
    success_url = reverse_lazy('listaCargos')
    #Borrar cargo
class CargoBorrar(DeleteView):
    model = Cargo
    template_name = os.path.join("defensaCivil", "confirmacionBorrado", "cargoBorrar.html")
    success_url = reverse_lazy('listaCargos')


# Elemento Views ------------------------------------------------------------------------------>
    #Ver Elementos
class listaElemento(ListView):
    model = Elementos
    template_name = os.path.join("defensaCivil", "listas", "listaElementos.html")
    context_object_name = 'elementos'
    paginate_by = 7
    def get_queryset(self):
        # Ordenar alfabéticamente por el atributo 'nombre'
        return Elementos.objects.all().order_by('nombre')
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
















# # Instituciones Views ------------------------------------------------------------------------------>
#     #Ver instituciones
class ListaInstitucion(ListView):
    model = Institucion
    template_name = os.path.join("defensaCivil", "listas", "listaInstituciones.html")
    context_object_name = 'instituciones'
    def get_queryset(self):
        # Ordenar alfabéticamente por el atributo 'nombre'
        return Institucion.objects.all().order_by('nombre')
#     #Crear instituciones
class InstitucionNueva(CreateView):
    model = Institucion
    form_class = InstitucionForm
    template_name = os.path.join("defensaCivil", "formularios", "institucionForm.html")
    success_url = reverse_lazy('listaInstituciones')

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset_persona = InstitucionPersonaFormSet()
        formset_elemento = InstitucionElementoFormSet()
        return self.render_to_response(self.get_context_data(form=form, formset_persona=formset_persona, formset_elemento=formset_elemento))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset_persona = InstitucionPersonaFormSet(request.POST)
        formset_elemento = InstitucionElementoFormSet(request.POST)

        if form.is_valid() and formset_persona.is_valid() and formset_elemento.is_valid():
            self.object = form.save()
            formset_persona.instance = self.object
            formset_persona.save()
            formset_elemento.instance = self.object
            formset_elemento.save()
            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(form=form, formset_persona=formset_persona, formset_elemento=formset_elemento))

# class InstitucionNueva(CreateView):
#     model = Institucion
#     form_class = InstitucionForm
#     template_name = os.path.join("defensaCivil", "formularios", "institucionForm.html")
#     success_url = reverse_lazy('listaInstituciones')
#     def get(self, request, *args, **kwargs):
#         self.object = None
#         form = self.get_form()
#         formset = InstitucionPersonaFormSet()
#         return self.render_to_response(self.get_context_data(form=form, formset=formset))
#     def post(self, request, *args, **kwargs):
#         self.object = None
#         form = self.get_form()
#         formset = InstitucionPersonaFormSet(request.POST)
#         if form.is_valid() and formset.is_valid():
#             self.object = form.save()
#             formset.instance = self.object
#             formset.save()
#             return redirect(self.success_url)
#         return self.render_to_response(self.get_context_data(form=form, formset=formset))

#     #Modificar instituciones
class InstitucionModificar(UpdateView):
    model = Institucion
    form_class = InstitucionForm
    template_name = os.path.join("defensaCivil", "formularios", "institucionForm.html")
    success_url = reverse_lazy('listaInstituciones')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset_persona = InstitucionPersonaFormSet(instance=self.object)
        formset_elemento = InstitucionElementoFormSet(instance=self.object)
        return self.render_to_response(self.get_context_data(form=form, formset_persona=formset_persona, formset_elemento=formset_elemento))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset_persona = InstitucionPersonaFormSet(request.POST, instance=self.object)
        formset_elemento = InstitucionElementoFormSet(request.POST, instance=self.object)

        if form.is_valid() and formset_persona.is_valid() and formset_elemento.is_valid():
            form.save()
            formset_persona.save()
            formset_elemento.save()
            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(form=form, formset_persona=formset_persona, formset_elemento=formset_elemento))

# class InstitucionModificar(UpdateView):
#     model = Institucion
#     form_class = InstitucionForm
#     template_name = os.path.join("defensaCivil", "formularios", "institucionForm.html")
#     success_url = reverse_lazy('listaInstituciones')
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         formset = InstitucionPersonaFormSet(instance=self.object)
#         return self.render_to_response(self.get_context_data(form=form, formset=formset))
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form = self.get_form()
#         formset = InstitucionPersonaFormSet(request.POST, instance=self.object)
#         if form.is_valid() and formset.is_valid():
#             form.save()
#             formset.save()
#             return redirect(self.success_url)
#         return self.render_to_response(self.get_context_data(form=form, formset=formset))

#     #Borrar instituciones
class InstitucionBorrar(DeleteView):
    model = Institucion
    template_name = os.path.join("defensaCivil", "confirmacionBorrado", "institucionBorrar.html")
    success_url = reverse_lazy('listaInstituciones')
        