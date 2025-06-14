from django import forms
from .models import Persona, Cargo, Categoria, Elementos, Institucion, InstitucionPersona, InstitucionElemento
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


 #FORMULARIO DE PERSONA (CREAR Y MODIFICAR)
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'dni', 'telefono', 'unica_area', 'id_cargo')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'unica_area': forms.CheckboxInput(attrs={'class': 'form-check-input form-control'}),
            'id_cargo': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {"nombre":"Nombre",
                  "dni":"D.N.I",
                  "telefono":"Teléfono",
                  "unica_area":"Unica Area",
                  "id_cargo":"Cargo o Labor",
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

    #FORMULARIO DE ELEMENTOS (CREAR Y MODIFICAR)
class ElementosForm(forms.ModelForm):
    class Meta:
        model = Elementos
        fields = ('nombre', 'descripcion', 'estado', 'cantidad', 'id_categoria', 'id_persona')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input form-control'}),
            'id_categoria': forms.Select(attrs={'class':'form-control'}),
            'id_persona': forms.Select(attrs={'class':'form-control'}),
        }
        labels = {"nombre":"Nombre",
                  "descripcion":"Descripción",
                  "cantidad":"Cantidad",
                  "estado":"Disponible",
                  "id_categoria":"Tipo",
                  "id_persona":"Persona a cargo",
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
class InstitucionElementoForm(forms.ModelForm):
    class Meta:
        model = InstitucionElemento
        fields = ("id_elemento",)
        widgets = {
            "id_elemento": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "id_elemento": "Elemento",
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
InstitucionElementoFormSet = inlineformset_factory(Institucion, InstitucionElemento, form=InstitucionElementoForm, extra=6)

   


        
