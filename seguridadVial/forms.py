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