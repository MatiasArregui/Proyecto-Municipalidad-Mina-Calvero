from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from .models import Elementos, Institucion, InstitucionCargoPersona,  Persona
from .forms import PersonaForm,ElementosForm, AuthenticationForm, InstitucionForm, InstitucionCargoPersonaForm, InstitucionCargoPersonaFormSet
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.db.models import ProtectedError
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
import os


# Pagina principal ----------------------------------------------------------------------------------->
def paginaPrincipal(request):
    try:
        elementos = list(Elementos.objects.all())
        instituciones = list(Institucion.objects.all())
        personas = list(Persona.objects.all())
        # Combinar y ordenar por un atributo común
        todo = sorted(elementos + instituciones + personas, key=lambda x: getattr(x, "nombre", getattr(x, "nombre_apellido", "")).lower())
        context = {"todo": todo}
        return render(request, template_name=os.path.join("defensaCivil", "paginaPrincipal.html"), context=context)
    except Exception as e:
        return render(request, template_name=os.path.join("defensaCivil", "paginaPrincipal.html"), context=None)
        



# Persona Views ------------------------------------------------------------------------------>
    #Ver Personas
class listaPersona(ListView):
    model = Persona
    template_name = os.path.join("defensaCivil", "listas", "listaPersonas.html")
    context_object_name = 'personas'
    paginate_by = 7
    def get_queryset(self):
        # Ordenar alfabéticamente por el atributo 'nombre'
        return Persona.objects.all().order_by('nombre_apellido')
    #Crear persona
class PersonaNueva(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = os.path.join("defensaCivil", "formularios", "personaForm.html")
    success_url = reverse_lazy('listaPersonas')
    
    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset_institucion_cargo = InstitucionCargoPersonaFormSet()
        return self.render_to_response(self.get_context_data(form=form, formset_institucion_cargo=formset_institucion_cargo))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset_institucion_cargo = InstitucionCargoPersonaFormSet(request.POST)
        if form.is_valid() and formset_institucion_cargo.is_valid():
            self.object = form.save()
            formset_institucion_cargo.instance = self.object
            formset_institucion_cargo.save()
            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(form=form, formset_institucion_cargo=formset_institucion_cargo))
    #Modificar persona
class PersonaModificar(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = os.path.join("defensaCivil", "formularios", "personaForm.html")
    success_url = reverse_lazy('listaPersonas')
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset_institucion_cargo = InstitucionCargoPersonaFormSet(instance=self.object)
        return self.render_to_response(self.get_context_data(form=form, formset_institucion_cargo=formset_institucion_cargo))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset_institucion_cargo = InstitucionCargoPersonaFormSet(request.POST, instance=self.object)

        if form.is_valid() and formset_institucion_cargo.is_valid():
            form.save()
            formset_institucion_cargo.save()
            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(form=form, formset_institucion_cargo=formset_institucion_cargo))
    #Borrar persona
class PersonaBorrar(DeleteView):
    model = Persona
    template_name = os.path.join("defensaCivil", "confirmacionBorrado", "personaBorrar.html")
    success_url = reverse_lazy('listaPersonas')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "No se puede eliminar esta persona porque tiene elementos relacionados.")
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)



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

# Instituciones Views ------------------------------------------------------------------------------>
#Ver instituciones
class ListaInstitucion(ListView):
    model = Institucion
    template_name = os.path.join("defensaCivil", "listas", "listaInstituciones.html")
    context_object_name = 'instituciones'
    paginate_by = 7
    def get_queryset(self):
        # Ordenar alfabéticamente por el atributo 'nombre'
        return Institucion.objects.all().order_by('nombre')


#     #Crear instituciones
class InstitucionNueva(CreateView):
    model = Institucion
    form_class = InstitucionForm
    template_name = os.path.join("defensaCivil", "formularios", "institucionForm.html")
    success_url = reverse_lazy('listaInstituciones')


#Detalle Factura ----------------->
def institucionDetalle(request, pk):
    institucion = Institucion.objects.get(id=pk)
    personas_institucion = [x.id_persona.pk for x in InstitucionCargoPersona.objects.filter(id_institucion=pk) ]
    personas = [ x for x in Persona.objects.all().order_by('nombre_apellido')  if x.pk in personas_institucion]
    cargos =  [{"id_persona": x.id_persona.pk, "cargo":x.cargo} for x in InstitucionCargoPersona.objects.filter(id_institucion=pk)]
  
    elementos_institucion = Elementos.objects.filter(id_institucion=pk)
    print(cargos)

    context= {"institucion":institucion, "personas": personas, "elementos": elementos_institucion, "cargos": cargos}
    return render(request, os.path.join("defensaCivil", "detalles", "institucionDetalle.html"), context=context)

#     #Modificar instituciones
class InstitucionModificar(UpdateView):
    model = Institucion
    form_class = InstitucionForm
    template_name = os.path.join("defensaCivil", "formularios", "institucionForm.html")
    success_url = reverse_lazy('listaInstituciones')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['institucion_id'] = self.object.id  # Obtener el ID de la institución
        id = self.get_object().id
        personas_institucion = [x.id_persona.pk for x in InstitucionCargoPersona.objects.filter(id_institucion=id) ]
        personas = [ x for x in Persona.objects.all().order_by('nombre_apellido') if x.pk in personas_institucion]
        print(personas)
        elementos_institucion = Elementos.objects.filter(id_institucion=id)
        print(personas_institucion)
        cargos =  [{"id_persona": x.id_persona.pk, "cargo":x.cargo} for x in InstitucionCargoPersona.objects.filter(id_institucion=id) ]
        context['cargos'] = cargos
        context['personas'] = personas
        context['elementos'] = elementos_institucion
        return context

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




# PARTE LOGICA DE LANDING PAGE (ACA DEFINIMOS LOS BLOQUES DE CODIGO PERTENECIENTES AL PROYECTO DE JORGE)
# Pagina principal ----------------------------------------------------------------------------------->
# def paginaPrincipal(request):
#     1 - PRIMERO BUSCAMOS AQUEL O AQUELLOS OBJETOS QUE SERAN PASADOS PARA SU USO EN EL TEMPLATE
#     elementos = Elementos.objects.all()
#     instituciones = Institucion.objects.all()
#     personas = Persona.objects.all()
#     # Combinar todos los conjuntos en una sola lista o QuerySet
#     todo = list(elementos) + list(instituciones) + list(personas)
#     2 - LUEGO CREAMOS LA VARIABLE CONTEXTO, QUE ES AQUEL QUE ALMACENE DENTRO DE SI MISMO, LA O LAS LISTAS QUE CONFORMARAN AL MISMO
#     context = {"todo": todo}
#     3 - ESTE RETURN DEVUELVE LA FUNCION RENDER QUE ESTA COMPUESTA POR TRES ARGUMENTOS: render(request, template_name=plantillaQueMostraraLaInformacion, context=variableQueAlmacenaLosDatos)
#     return render(request, template_name= os.path.join("defensaCivil", "paginaPrincipal.html"), context=context)
#     4 - context= {"nombreVariable":variableQueGuardoLaQuery}. ej: query: personas = Persona.objects.all() context: context = {"personas": personas}

# Pagina principal Landing Page----------------------------------------------------------------------------------->
# definan la funcion que mostrara su landing page

