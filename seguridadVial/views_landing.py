# -- Django resources --
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse_lazy

# -- Models importations --
from .models import Catastrophe, Protocole, Refujio, Institucion, PdfFrame, CatPdf, SubCatastrofe, Protocolo, Prevencion, IntegrantesDC

from .forms import ProtocoleFormset, RefujioFormset, CatastropheForm, PdfFrameForm, CatPdfform, PdfCatFormset, SubCatastrofeForm, ProtocolosForm, PrevencionForm

# -- Views -- 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
import os


class PdfFrameDeleteView(DeleteView):
    model = PdfFrame
    context_object_name = "pdf"   
    template_name = os.path.join("defensaCivil", "confirmacionBorrado", "pdf_eliminar.html")
    success_url = reverse_lazy('Lista-Desastre')

class PdfFrameCreateView(CreateView):
    model = PdfFrame
    form_class = PdfFrameForm
    template_name = os.path.join("defensaCivil", "formularios", "pdf_create_update.html")
    success_url = reverse_lazy('Lista-Desastre')

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        cat_formset = PdfCatFormset()
        return self.render_to_response(self.get_context_data(form=form, cat_formset=cat_formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        cat_formset = PdfCatFormset(request.POST)

        if form.is_valid() and cat_formset.is_valid():
            self.object = form.save()
            cat_formset.instance = self.object
            cat_formset.save()
            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(form=form, cat_formset=cat_formset))


class PdfFrameUpdateView(UpdateView):
    model = PdfFrame
    form_class = PdfFrameForm
    template_name = os.path.join("defensaCivil", "formularios", "pdf_create_update.html")
    success_url = reverse_lazy('Lista-Desastre')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        cat_formset = PdfCatFormset(instance=self.object)
        return self.render_to_response(self.get_context_data(form=form, cat_formset=cat_formset))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        cat_formset = PdfCatFormset(request.POST, instance=self.object)

        if form.is_valid() and cat_formset.is_valid():
            form.save()
            cat_formset.save()
            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(form=form, cat_formset=cat_formset))

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
    return render(request, template_name=os.path.join("defensaCivil", "listas", "dashboard.html"), 
                  context={"disaster":Catastrophe.objects.all(), "active":active, "pdf":PdfFrame.objects.all(), "subcat": SubCatastrofe.objects.all(), "integrantes":IntegrantesDC.objects.all()})

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
# def ActiveCatastropheListView(request):
    
#     template = os.path.join("landingPage", "index_public.html")

#     all_disaster = Catastrophe.objects.filter(is_default=False)
#     filters_is_active = Catastrophe.objects.filter(is_active=True)
#     if not filters_is_active: 
#         cat = Catastrophe.objects.get(is_default=True) 

#         # Obtengo todas las pk de las instituciones en refugios
#         all_cat = [x.institucion.pk for x in Refujio.objects.all() ]
#         # Muestro en la pagina estandard solo aquellas areas pertenecientes a una catastrofe
#         ref = [x for x in Institucion.objects.all() if x.pk in all_cat]
        
#     else:
#         cat = Catastrophe.objects.get(is_active=True)
#         ref = Refujio.objects.filter(catastrofe=cat)
#         pdf_cat = [x.id_pdf.pk for x in CatPdf.objects.filter(id_cat=cat.pk)]
#         frame = [{"url":x.url} for x in PdfFrame.objects.all() if x.pk in pdf_cat ]
#         print(frame)
        
  
#     pro = Protocole.objects.filter(catastrophe=cat)



#     context = {"catastrofe": cat , "protocolo":pro, "refujio":ref, "all": all_disaster, "frame":frame}
import re


def ActiveCatastropheListView(request):
    template = os.path.join("landingPage", "index_public.html")
    all_disaster = Catastrophe.objects.filter(is_default=False)
    filters_is_active = Catastrophe.objects.filter(is_active=True)

    if not filters_is_active:
        cat = Catastrophe.objects.get(is_default=True)
        institucionesDC = IntegrantesDC.objects.all()
        all_cat = [x.institucion.pk for x in Refujio.objects.all()]
        ref = [x for x in Institucion.objects.all() if x.pk in all_cat]
        pdf_frames = []
        print(cat.descripcion)
        try: 
            institucion = Institucion.objects.get(id=2)
        except Exception as e:
            institucion = Institucion.objects.get()
        pro = Protocole.objects.filter(catastrophe=cat)
        context = {
        "catastrofe": cat,
        "protocolo": pro,
        "refujio": ref,
        "all": all_disaster,
        "pdf_frames": pdf_frames,
        "institucion":institucion,
        "instituciones":institucionesDC
        }
    else:
        cat = Catastrophe.objects.get(is_active=True)
        ref = Refujio.objects.filter(catastrofe=cat)
        pdf_relaciones = CatPdf.objects.filter(id_cat=cat.pk)

        pdf_frames = []
        for rel in pdf_relaciones:
            url = rel.id_pdf.url
            name = rel.id_pdf.name
            match = re.search(r"/d/([^/]+)/", url)
            if match:
                file_id = match.group(1)
                pdf_frames.append({
                    "file_id": file_id,
                    "name": name
                })
        pro = Protocole.objects.filter(catastrophe=cat)
        context = {
        "catastrofe": cat,
        "protocolo": pro,
        "refujio": ref,
        "all": all_disaster,
        "pdf_frames": pdf_frames
        }




    return render(request, template, context)



from .models import SubCatastrofe
from .forms import SubCatastrofeForm, PrevencionFormSet, ProtocoloFormSet, IntegrantesDCForm

class SubCatastrofeCreateView(CreateView):
    model = SubCatastrofe
    form_class = SubCatastrofeForm
    template_name =  os.path.join("defensaCivil", "formularios", 'crear_subcatastrofe.html') # Asegurate de tener este template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['PrevencionFormSet'] = PrevencionFormSet(self.request.POST)
            context['ProtocoloFormSet'] = ProtocoloFormSet(self.request.POST)
        else:
            context['PrevencionFormSet'] = PrevencionFormSet()
            context['ProtocoloFormSet'] = ProtocoloFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        prev_formset = context['PrevencionFormSet']
        prot_formset = context['ProtocoloFormSet']
        if prev_formset.is_valid() and prot_formset.is_valid():
            self.object = form.save()
            prev_formset.instance = self.object
            prot_formset.instance = self.object
            prev_formset.save()
            prot_formset.save()
            return redirect("Lista-Desastre")  # Ajusta según tu URL
        else:
            return self.form_invalid(form)


class SubCatastrofeUpdateView(UpdateView):
    model = SubCatastrofe
    form_class = SubCatastrofeForm
    template_name = os.path.join("defensaCivil", "formularios", "crear_subcatastrofe.html")  # Usás el mismo template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["PrevencionFormSet"] = PrevencionFormSet(self.request.POST, instance=self.object)
            context["ProtocoloFormSet"] = ProtocoloFormSet(self.request.POST, instance=self.object)
        else:
            context["PrevencionFormSet"] = PrevencionFormSet(instance=self.object)
            context["ProtocoloFormSet"] = ProtocoloFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        prev_formset = context["PrevencionFormSet"]
        prot_formset = context["ProtocoloFormSet"]
        if prev_formset.is_valid() and prot_formset.is_valid():
            self.object = form.save()
            prev_formset.instance = self.object
            prot_formset.instance = self.object
            prev_formset.save()
            prot_formset.save()
            return redirect("Lista-Desastre")  # Cambiá esto según tu URL
        else:
            return self.form_invalid(form)
        
class SubCatastrofeDeleteView(DeleteView):
    model = SubCatastrofe
    template_name = os.path.join("defensaCivil", "formularios", "delete.html") 
    success_url = reverse_lazy("Lista-Desastre")
    
def SubCatastrofe_vista(request, pk):
    subcatastrofe = get_object_or_404(SubCatastrofe, id=pk)

    # Accedemos a prevenciones y protocolos usando related_name
    prevenciones = subcatastrofe.prevenciones.all()
    protocolos = subcatastrofe.protocolos.all()

    contexto = {
        'subcatastrofe': subcatastrofe,
        'prevenciones': prevenciones,
        'protocolos': protocolos
    }
    print(prevenciones, protocolos)


    return render(request, os.path.join("landingPage", "subcatastrofe.html"), contexto)
# Vistas de integrantes dc ------------------------------------------------------------------------------>

    #Crear integrantes
class IntegranteNuevo(CreateView):
    model = IntegrantesDC
    form_class = IntegrantesDCForm
    context_object_name = "integrante"  
    template_name = os.path.join("defensaCivil", "formularios", "integrantesdc.html")
    success_url = reverse_lazy('Lista-Desastre')
    #Modificar integrante
class IntegranteModificar(UpdateView):
    model = IntegrantesDC
    form_class = IntegrantesDCForm
    context_object_name = "integrante"  
    template_name = os.path.join("defensaCivil", "formularios", "integrantesdc.html")
    success_url = reverse_lazy('Lista-Desastre')
    #Borrar integrante
class IntegranteBorrar(DeleteView):
    model = IntegrantesDC
    context_object_name = "integrante"  
    template_name = os.path.join("defensaCivil", "confirmacionBorrado", "integrantedcBorrar.html")
    success_url = reverse_lazy('Lista-Desastre')
