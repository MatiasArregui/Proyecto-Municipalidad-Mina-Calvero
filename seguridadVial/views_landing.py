from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from .models import Cargo, Elementos, Institucion, InstitucionPersona, Persona
from .forms import PersonaForm, CargoForm,  ElementosForm, AuthenticationForm, InstitucionForm, InstitucionPersonaForm, InstitucionPersonaFormSet
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.db.models import ProtectedError
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
import os

def landingPage(request):
    return render(request, template_name= os.path.join("landingPage", "pagPrincipal.html"), context=None)
def catastrofes(request):
    return render(request, template_name= os.path.join("landingPage", "catastrofes.html"), context=None)
def protocolosEmergencia(request):
    return render(request, template_name= os.path.join("landingPage", "protocolos.html"), context=None)
def integrantesDefCivil(request):
    return render(request, template_name= os.path.join("landingPage", "areas.html"), context=None)
def mapa(request):
    return render(request, template_name= os.path.join("landingPage", "mapa.html"), context=None)