from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={
         
            'placeholder': 'Nombre de usuario',
            'autocomplete': 'username' 
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'input__field',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password',
            'style':"border:none;"
        })
    )

    # Personalizar los mensajes de error
    error_messages = {
        'invalid_login': "Usuario o contraseña incorrectos. Por favor, inténtelo nuevamente.",
        'inactive': "Esta cuenta está inactiva. Contacte al administrador para más información.",
    }
