from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from .models import Cargo, Categoria, Elementos, Institucion, InstitucionPersona, Persona
from .forms import PersonaForm, CargoForm, CategoriaForm, AuthenticationForm, InstitucionForm, InstitucionPersonaForm, InstitucionPersonaFormSet
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.db.models import ProtectedError
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
import os


# Persona Views ------------------------------------------------------------------------------>
    #Ver Personas
class listaPersona(ListView):
    model = Persona
    template_name = os.path.join("listas", "listaPersonas.html")
    context_object_name = 'personas'
    paginate_by = 7
    #Crear persona
class PersonaNueva(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = os.path.join("formularios", "personaForm.html")
    success_url = reverse_lazy('listaPersonas')
    #Modificar persona
class PersonaModificar(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = os.path.join("formularios", "personaForm.html")
    success_url = reverse_lazy('listaPersonas')
    #Borrar persona
class PersonaBorrar(DeleteView):
    model = Persona
    template_name = os.path.join("confirmacionBorrado", "personaBorrar.html")
    success_url = reverse_lazy('listaPersonas')
    
# Elemento Views ------------------------------------------------------------------------------>
    #Ver Elementos
class listaElemento(ListView):
    model = Elementos
    template_name = os.path.join("listas", "listaPersonas.html")
    context_object_name = 'personas'
    paginate_by = 7
    #Crear persona
class PersonaNueva(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = os.path.join("formularios", "personaForm.html")
    success_url = reverse_lazy('listaPersonas')
    #Modificar persona
class PersonaModificar(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = os.path.join("formularios", "personaForm.html")
    success_url = reverse_lazy('listaPersonas')
    #Borrar persona
class PersonaBorrar(DeleteView):
    model = Persona
    template_name = os.path.join("confirmacionBorrado", "personaBorrar.html")
    success_url = reverse_lazy('listaPersonas')




        