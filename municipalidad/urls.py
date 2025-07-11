"""
URL configuration for municipalidad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth.decorators import login_required, permission_required
from .forms import LoginForm
from django.contrib.auth.views import LoginView
import os


urlpatterns = [
    path('admin/', admin.site.urls),
    # Login ----------------------------------------------------------------------------------->
   
    path('login/', LoginView.as_view(
        template_name=os.path.join("registration", "login.html"),
        authentication_form=LoginForm
    ), name='ingreso'),
    path("", include("seguridadVial.urls")),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)