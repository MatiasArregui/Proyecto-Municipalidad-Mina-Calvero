from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from .models import Cargo, Categoria, Elementos, Institucion, InstitucionPersona, Persona
from .forms import PersonaForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.db.models import ProtectedError
from django.views.generic import ListView, CreateView, DeleteView
import os


# Persona Views ------------------------------------------------------------------------------
class listaPersona(ListView):
    model = Persona
    template_name = os.path.join("listas", "listaPersonas.html")
    context_object_name = 'personas'
    paginate_by = 7
    
        