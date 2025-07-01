# -- Django resources --
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse_lazy
# -- Models importations --
from .models import Catastrophe, Protocole, Refujio, Institucion, PdfFrame
from .forms import ProtocoleFormset, RefujioFormset, CatastropheForm, PdfFrameForm

# -- Views -- 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
import os


class PdfFrameDeleteView(DeleteView):
    model = PdfFrame
    template_name = os.path.join("defensaCivil", "formularios", "pdf_eliminar.html")
    success_url = reverse_lazy('Lista-Desastre')

class PdfFrameCreateView(CreateView):
    model = PdfFrame
    form_class = PdfFrameForm
    template_name = os.path.join("defensaCivil", "formularios", "pdf_create_update.html")
    success_url = reverse_lazy('Lista-Desastre')

class PdfFrameUpdateView(UpdateView):
    model = PdfFrame
    form_class = PdfFrameForm
   
    template_name = os.path.join("defensaCivil", "formularios", "pdf_create_update.html")
    success_url = reverse_lazy('Lista-Desastre')
# --- Catastrofes  ----

def DetalleCatastrofe(request, pk):
    template = os.path.join("landingPage", "catastrofes.html")

    cat = Catastrophe.objects.get(pk=pk)
    all_inst = [x.institucion.pk for x in Refujio.objects.filter(catastrofe=cat)]
    ref = [x for x in Institucion.objects.all() if x.pk in all_inst]
    pro = Protocole.objects.filter(catastrophe=cat)
    print(ref)
    context = {"catastrofe": cat , "protocolo":pro, "area":ref}
    
    return render(request, template_name=template, context=context)




# <--  Admin view -->
class DeleteDisaster(DeleteView):
    model = Catastrophe
    template_name = os.path.join('defensaCivil', 'formularios', 'delete.html')
    success_url = '/listaDesastre/'

class CatastropheCreateView(CreateView):
    model = Catastrophe
    form_class = CatastropheForm
    template_name = os.path.join("defensaCivil", "formularios", "create.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocole_formset'] = ProtocoleFormset()
        context['refujio_formset'] = RefujioFormset()

        return context

    def post(self, request, *args, **kwargs):
        form = CatastropheForm(request.POST)
        protocole_formset = ProtocoleFormset(request.POST)
        refujio_formset = RefujioFormset(request.POST)

        if form.is_valid() and protocole_formset.is_valid() and refujio_formset.is_valid():

            catastrophe = form.save()

            protocole_formset.instance = catastrophe
            refujio_formset.instance = catastrophe

            protocole_formset.save()
            refujio_formset.save()

            return redirect('Lista-Desastre')

        return render(request, self.template_name, {
            'form': form,
            'protocole_formset': protocole_formset,
            'refujio_formset': refujio_formset,
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
        else:
            context['protocole_formset'] = ProtocoleFormset(instance=self.object)
            context['refujio_formset'] = RefujioFormset(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = CatastropheForm(request.POST, instance=self.object)
        protocole_formset = ProtocoleFormset(request.POST, instance=self.object)
        refujio_formset = RefujioFormset(request.POST, instance=self.object)


        if form.is_valid() and protocole_formset.is_valid() and refujio_formset.is_valid():
            form.save()
            protocole_formset.save()
            refujio_formset.save()
            return redirect('Lista-Desastre')

        return render(request, self.template_name, {
            'form': form,
            'protocole_formset': protocole_formset,
            'refujio_formset': refujio_formset,
        })

# Admin view for disaster control
def DashboardCatastrophe(request):
    active = True
    if Catastrophe.objects.filter(is_active=True):
        active = False
    return render(request, template_name=os.path.join("defensaCivil", "listas", "dashboard.html"), context={"disaster":Catastrophe.objects.all(), "active":active, "pdf":PdfFrame.objects.all()})

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

        # Obtengo todas las pk de las instituciones en refugios
        all_cat = [x.institucion.pk for x in Refujio.objects.all() ]
    

        # Muestro en la pagina estandard solo aquellas areas pertenecientes a una catastrofe
        ref = [x for x in Institucion.objects.all() if x.pk in all_cat]
        
    else:
        cat = Catastrophe.objects.get(is_active=True)
        ref = Refujio.objects.filter(catastrofe=cat)
    
    pro = Protocole.objects.filter(catastrophe=cat)
  


    context = {"catastrofe": cat , "protocolo":pro, "refujio":ref, "all": all_disaster}

    # -- as view
    print("--------------------------------")
    print("catastrofe",[cat.image_disaster])
    print("protocole_formset: ",[pro])
    print("refujio_formset: ",[ref])
    print("--------------------------------")

    return render(request, template_name=template, context=context)

