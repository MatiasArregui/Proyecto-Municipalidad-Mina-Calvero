# -- Django resources --
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.db.models import ProtectedError

# -- Models importations --
from .models import Catastrophe, Protocole, Refujio, Footer_info
from .forms import ProtocoleFormset, RefujioFormset, FooterInfoFormset, CatastropheForm

# -- Views -- 
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

# <--  Vistas Santy  -->
class CatastropheCreateView(CreateView):
    model = Catastrophe
    form_class = CatastropheForm
    template_name = os.path.join("landingPage", "Forms", "create.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocole_formset'] = ProtocoleFormset()
        context['refujio_formset'] = RefujioFormset()
        context['footer_formset'] = FooterInfoFormset()

        return context

    def post(self, request, *args, **kwargs):
        form = CatastropheForm(request.POST)
        protocole_formset = ProtocoleFormset(request.POST)
        refujio_formset = RefujioFormset(request.POST)
        footer_formset = FooterInfoFormset(request.POST)

        if form.is_valid() and footer_formset.is_valid() and protocole_formset.is_valid() and refujio_formset.is_valid():

            catastrophe = form.save()

            protocole_formset.instance = catastrophe
            refujio_formset.instance = catastrophe
            footer_formset.instance = catastrophe

            protocole_formset.save()
            refujio_formset.save()
            footer_formset.save()

            return redirect('/defensaCivil/Lista-Desastre/')

        return render(request, self.template_name, {
            'form': form,
            'protocole_formset': protocole_formset,
            'refujio_formset': refujio_formset,
            'footer_formset': footer_formset
        })

class CatastropheUpdateView(UpdateView):
    model = Catastrophe
    form_class = CatastropheForm
    template_name = os.path.join("Forms", "update.html")

    def get_object(self):
        return get_object_or_404(Catastrophe, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['protocole_formset'] = ProtocoleFormset(self.request.POST, instance=self.object)

            context['refujio_formset'] = RefujioFormset(self.request.POST, instance=self.object)

            context['footer_formset'] = FooterInfoFormset(self.request.POST, instance=self.object)
        else:
            context['protocole_formset'] = ProtocoleFormset(instance=self.object)
            context['refujio_formset'] = RefujioFormset(instance=self.object)
            context['footer_formset'] = FooterInfoFormset(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = CatastropheForm(request.POST, instance=self.object)
        protocole_formset = ProtocoleFormset(request.POST, instance=self.object)
        refujio_formset = RefujioFormset(request.POST, instance=self.object)
        footer_formset = FooterInfoFormset(request.POST, instance=self.object)

        if form.is_valid() and protocole_formset.is_valid() and refujio_formset.is_valid() and footer_formset.is_valid():
            
            form.save()
            protocole_formset.save()
            refujio_formset.save()
            footer_formset.save()

            return redirect('/defensaCivil/Lista-Desastre/')

        return render(request, self.template_name, {
            'form': form,
            'protocole_formset': protocole_formset,
            'refujio_formset': refujio_formset,
            'footer_formset': footer_formset
        })

# Admin view for disaster control
def DashboardCatastrophe(request):
    return render(request, template_name=os.path.join("landingPage", "dashboard.html"), context={"disaster":Catastrophe.objects.all()})

# Landing page defaulte view
def ActiveCatastropheListView(request):
    
    template = os.path.join("landingPage", "pagPrincipal.html")
    cat = Catastrophe.objects.filter(is_active=True)
    pro = Protocole.objects.filter(catastrophe__in=cat)
    ref = Refujio.objects.filter(catastrophe__in=cat)
    foo = Footer_info.objects.filter(catastrophe__in=cat)
    context = {"catastrophe": cat , "protocole":pro, "refujio":ref, "footer": foo}

    return render(request, template_name=template, context=context)

