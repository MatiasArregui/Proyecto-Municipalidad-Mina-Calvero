from django import forms
from .models import Persona, Cargo, Categoria, Elementos, Institucion, InstitucionPersona
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
        fields = ('nombre', 'descripcion', 'estado', 'id_categoria', 'id_institucion', 'id_persona')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input form-control'}),
            'id_categoria': forms.Select(attrs={'class':'form-control'}),
            'id_institucion': forms.Select(attrs={'class':'form-control'}),
            'id_persona': forms.Select(attrs={'class':'form-control'}),
        }
        labels = {"nombre":"Nombre",
                  "descripcion":"Descripción",
                  "estado":"Disponible",
                  "id_categoria":"Tipo",
                  "id_institucion":"Institucion perteneciente",
                  "id_persona":"Persona a cargo",
            }

    #FORMULARIO DE CATEGORIAS (CREAR Y MODIFICAR)
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ("nombre",)
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "nombre": "Nombre",
        }
        
    #FORMULARIO DE INSTITUCION Y PERSONA IN-LINE (CREAR, MODIFICAR)
class InstitucionPersonaForm(forms.ModelForm):
    class Meta:
        model = InstitucionPersona
        fields = ("id_persona",)
        widgets = {
            "id_persona": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "id_persona": "Persona",
        }
    #FORMULARIO DE INSTITUCION (CREAR, MODIFICAR)
class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ('nombre', 'id_persona_encargado', 'mail', 'descripcion', 'direccion', 'telefono')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'id_persona_encargado': forms.Select(attrs={"class": "form-control"}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {"nombre":"Nombre",
                  'id_persona_encargado':'Encargado',
                  "mail":"Mail",
                  "descripcion":"Descripción",
                  "direccion":"Direccion",
                  "telefono":"Telefono",
            }

InstitucionPersonaFormSet = inlineformset_factory(Institucion, InstitucionPersona, form=InstitucionPersonaForm, extra=6)

    #FORMULARIO DE PERSONA (CREAR Y MODIFICAR)
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'dni', 'telefono', 'id_cargo')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'id_cargo': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {"nombre":"Nombre",
                  "dni":"D.N.I",
                  "telefono":"Teléfono",
                  "id_cargo":"Cargo o Labor",
            }

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
        
