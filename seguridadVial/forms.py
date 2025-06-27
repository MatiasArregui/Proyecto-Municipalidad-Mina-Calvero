from django import forms
from .models import Persona, Elementos, Institucion, InstitucionCargoPersona, Catastrophe, Protocole, Refujio
from django.forms import inlineformset_factory
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
            'autocomplete': 'username' 
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password' 
        })
    )

    # Personalizar los mensajes de error
    error_messages = {
        'invalid_login': "Usuario o contraseña incorrectos. Por favor, inténtelo nuevamente.",
        'inactive': "Esta cuenta está inactiva. Contacte al administrador para más información.",
    }


#FORMULARIO DE ELEMENTOS (CREAR Y MODIFICAR)
class ElementosForm(forms.ModelForm):
    class Meta:
        model = Elementos
        fields = ("nombre", "tipo", "descripcion", "cantidad", "observaciones", "estado", "id_institucion", "id_persona")
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input form-control'}),
            'id_persona': forms.Select(attrs={'class':'form-control'}),
            'id_institucion': forms.Select(attrs={'class':'form-control'}),
        }
        labels = {
            "nombre":"Nombre",
            "tipo":"Tipo",
            "descripcion":"Descripción",
            "cantidad":"Cantidad",
            "estado":"Ocupado",
            "id_persona":"Responsable",
            "id_institucion":"Institucion perteneciente",
        }


#FORMULARIO DE INSTITUCION (CREAR, MODIFICAR)
class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ("nombre", "direccion", "email", "telefono", "descripcion")
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            "nombre":"Nombre",
            "direccion":"Dirección",
            "email":"Email",
            "telefono":"Teléfono",
            "descripcion":"Descripción",
        }
        
#FORMULARIO DE CARGO E INSTITUCION IN-LINE (CREAR, MODIFICAR)
class InstitucionCargoPersonaForm(forms.ModelForm):
    class Meta:
        model = InstitucionCargoPersona
        fields = ("id_institucion", "cargo")
        widgets = {
            "id_institucion": forms.Select(attrs={"class": "form-control select_insti"}),
            "cargo": forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "id_institucion": "Institución",
            "cargo": "Cargo",
        }

        
#FORMULARIO DE PERSONA (CREAR Y MODIFICAR)
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre_apellido', 'dni', 'telefono')
        widgets = {
            'nombre_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "nombre_apellido":"Nombre y Apellido",
            "dni":"D.N.I",
            "telefono":"Teléfono",
        }



InstitucionCargoPersonaFormSet = inlineformset_factory(Persona, InstitucionCargoPersona, form=InstitucionCargoPersonaForm, extra=2)



# <---------  landing forms  ---------->
class ProtocoleForm(forms.ModelForm):
    class Meta:
        model = Protocole
        fields = ("campo_seleccion", "name",)
        widgets = {
            "campo_seleccion": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "campo_seleccion": "Estado Del Protocolo",
            "name":"Descripción de protocolo",
        }


class RefujioForm(forms.ModelForm):
    class Meta:
        model = Refujio
        fields = ['institucion']
        labels = {
            'institucion': 'Area Relacionada | Catastrofe',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control select_insti'})
        

class CatastropheForm(forms.ModelForm):
    class Meta:
        model = Catastrophe
        fields = ("type_disaster", "image_disaster", "descripcion", "mapa_interactivo")
        widgets = {
            "type_disaster": forms.TextInput(attrs={"class": "form-control"}),
            "image_disaster": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows":"3"}),
            "mapa_interactivo": forms.TextInput(attrs={"class": "form-control"}),

        }
        labels = {
            "type_disaster": "Nombre Catástrofe",
            "image_disaster":"Imagen Cabecera de Página",
            "descripcion":"Texto de Cabecera",
            "mapa_interactivo" : "Enlace o hipervínculo a mapa interactivo",
        }

        

# Formset -> inlines 
ProtocoleFormset = inlineformset_factory(Catastrophe, Protocole, form=ProtocoleForm, extra=5)
RefujioFormset = inlineformset_factory(Catastrophe, Refujio, form=RefujioForm, extra=5)


