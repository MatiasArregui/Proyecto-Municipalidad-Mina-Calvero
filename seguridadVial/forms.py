from django import forms
from .models import Persona, Cargo, Elementos, Institucion, InstitucionCargoPersona, Catastrophe, Protocole, Refujio
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
        fields = ("nombre", "direccion", "email", "telefono")
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "nombre":"Nombre",
            "direccion":"Dirección",
            "email":"Email",
            "telefono":"Teléfono",
        }
        
#FORMULARIO DE CARGO E INSTITUCION IN-LINE (CREAR, MODIFICAR)
class InstitucionCargoPersonaForm(forms.ModelForm):
    class Meta:
        model = InstitucionCargoPersona
        fields = ("id_institucion", "id_cargo")
        widgets = {
            "id_institucion": forms.Select(attrs={"class": "form-control"}),
            "id_cargo": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "id_institucion": "Institución",
            "id_cargo": "Cargo",
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


#FORMULARIO DE CARGO (CREAR Y MODIFICAR)
class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ("nombre",)
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "nombre": "Nombre",
        }
# <---------  landing forms  ---------->

class ProtocoleForm(forms.ModelForm):
    class Meta:
        model = Protocole
        fields = '__all__'

class RefujioForm(forms.ModelForm):
    class Meta:
        model = Refujio
        fields = '__all__'

class CatastropheForm(forms.ModelForm):
    class Meta:
        model = Catastrophe
        fields = '__all__'

# Formset -> inlines 
ProtocoleFormset = inlineformset_factory(Catastrophe, Protocole, form=ProtocoleForm, extra=5)
RefujioFormset = inlineformset_factory(Catastrophe, Refujio, form=RefujioForm, extra=5)
