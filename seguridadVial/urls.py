from django.contrib import admin
from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth.views import LoginView
# from .forms import LoginForm
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    # Login ----------------------------------------------------------------------------------->
    path('', LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=LoginForm
    ), name='login'),
    # Les dejo un ejemplo --------------------------------------------------------------------------------->
    # path("ordenes/", login_required(permission_required('miAplicacion.view_orden')(views.listaOrdenes.as_view())), name="listaOrdenes"),
    path("personas/", login_required(permission_required('miAplicacion.view_orden')(views.listaPersona.as_view())), name="listaPersonas"),
]