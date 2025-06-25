# -- Django resources --
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404

# -- Models importations --
from .models import Catastrophe, Protocole, Refujio, Footer_info
from .forms import ProtocoleFormset, RefujioFormset, FooterInfoFormset, CatastropheForm, UrlFormset, url_map

# -- Views -- 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
import os

# <-- Public Views -->
def landingPage(request):
    return render(request, template_name= os.path.join("landingPage", "index_public.html"), context=None)

def catastrofes(request):
    return render(request, template_name= os.path.join("landingPage", "catastrofes.html"), context=None)
def protocolosEmergencia(request):
    return render(request, template_name= os.path.join("landingPage", "protocolos.html"), context=None)
def integrantesDefCivil(request):
    return render(request, template_name= os.path.join("landingPage", "areas.html"), context=None)
def mapa(request):
    return render(request, template_name= os.path.join("landingPage", "mapa.html"), context=None)

# <--  Admin view -->
class DeleteDisaster(DeleteView):
    model = Catastrophe
    template_name = os.path.join('defensaCivil', 'formularios', 'delete.html')
    success_url = '/Lista-Desastre/'

class CatastropheCreateView(CreateView):
    model = Catastrophe
    form_class = CatastropheForm
    template_name = os.path.join("defensaCivil", "formularios", "create.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocole_formset'] = ProtocoleFormset()
        context['refujio_formset'] = RefujioFormset()
        context['footer_formset'] = FooterInfoFormset()
        context['url_formset'] = UrlFormset()

        return context

    def post(self, request, *args, **kwargs):
        form = CatastropheForm(request.POST)
        protocole_formset = ProtocoleFormset(request.POST)
        refujio_formset = RefujioFormset(request.POST)
        footer_formset = FooterInfoFormset(request.POST)
        url_formset = UrlFormset(request.POST)

        if form.is_valid() and footer_formset.is_valid() and protocole_formset.is_valid() and refujio_formset.is_valid() and url_formset.is_valid():

            catastrophe = form.save()

            protocole_formset.instance = catastrophe
            refujio_formset.instance = catastrophe
            footer_formset.instance = catastrophe
            url_formset.instance = catastrophe

            protocole_formset.save()
            refujio_formset.save()
            footer_formset.save()
            url_formset.save()

            return redirect('Lista-Desastre')

        return render(request, self.template_name, {
            'form': form,
            'protocole_formset': protocole_formset,
            'refujio_formset': refujio_formset,
            'footer_formset': footer_formset,
            'url_formset': url_formset
        })



class CatastropheUpdateView(UpdateView):
    model = Catastrophe
    form_class = CatastropheForm
    template_name = os.path.join("defensaCivil", "formularios", "update.html")

    def get_object(self):
        return get_object_or_404(Catastrophe, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['protocole_formset'] = ProtocoleFormset(self.request.POST, instance=self.object)
            context['refujio_formset'] = RefujioFormset(self.request.POST, instance=self.object)
            context['footer_formset'] = FooterInfoFormset(self.request.POST, instance=self.object)
            context['url_formset'] = UrlFormset(self.request.POST, instance=self.object)
        else:
            context['protocole_formset'] = ProtocoleFormset(instance=self.object)
            context['refujio_formset'] = RefujioFormset(instance=self.object)
            context['footer_formset'] = FooterInfoFormset(instance=self.object)
            context['url_formset'] = UrlFormset(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = CatastropheForm(request.POST, instance=self.object)
        protocole_formset = ProtocoleFormset(request.POST, instance=self.object)
        refujio_formset = RefujioFormset(request.POST, instance=self.object)
        footer_formset = FooterInfoFormset(request.POST, instance=self.object)
        url_formset = UrlFormset(request.POST, instance=self.object)

        if form.is_valid() and protocole_formset.is_valid() and refujio_formset.is_valid() and footer_formset.is_valid() and url_formset.is_valid():
            
            form.save()
            protocole_formset.save()
            refujio_formset.save()
            footer_formset.save()
            url_formset.save()

            return redirect('Lista-Desastre')

        return render(request, self.template_name, {
            'form': form,
            'protocole_formset': protocole_formset,
            'refujio_formset': refujio_formset,
            'footer_formset': footer_formset,
            'url_formset': url_formset
        })

# Admin view for disaster control
def DashboardCatastrophe(request):
    active = True
    if Catastrophe.objects.filter(is_active=True):
        active = False
    return render(request, template_name=os.path.join("defensaCivil", "listas", "dashboard.html"), context={"disaster":Catastrophe.objects.all(), "active":active})

# Confirm to activate disaster
def ActiveDisaster(request, pk):
    if request.method == "POST":
        disaster = Catastrophe.objects.get(id=pk)
        if disaster.is_active:
            disaster.is_active = False
            disaster.save()
        else:
            disaster.is_active = True
            disaster.save()
        return redirect('Lista-Desastre')

    else:
        return render(request, template_name=os.path.join("defensaCivil", "formularios", "active.html"), context=None)

# Landing page defaulte view
def ActiveCatastropheListView(request):
    
    template = os.path.join("landingPage", "index_public.html")

    all_disaster = Catastrophe.objects.filter(is_default=False)
    filters_is_active = Catastrophe.objects.filter(is_active=True)
    if not filters_is_active: 
        cat = Catastrophe.objects.get(is_default=True) 
    else:
        cat = Catastrophe.objects.get(is_active=True)
    
    pro = Protocole.objects.filter(catastrophe=cat)
    ref = Refujio.objects.filter(catastrophe=cat)
    foo = Footer_info.objects.filter(catastrophe=cat)
    maps =  url_map.objects.filter(catastrophe=cat)


    context = {"catastrofe": cat , "protocolo":pro, "refujio":ref, "footer": foo, "maps": maps, "all": all_disaster}

    # -- as view
    print("--------------------------------")
    print("catastrofe",[cat.image_disaster])
    print("protocole_formset: ",[pro])
    print("refujio_formset: ",[ref])
    print("footer_formset: ",[foo])
    print("map_formset:",[maps])
    print("--------------------------------")

    return render(request, template_name=template, context=context)

