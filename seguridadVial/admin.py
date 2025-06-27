from django.contrib import admin
from .models import Elementos, Institucion, InstitucionCargoPersona, Persona, Catastrophe, Protocole, Refujio
admin.site.register(Institucion)
admin.site.register(Elementos)

# INLINE DETALLE  ---------------------------->
class InstitucionPersonaInline(admin.TabularInline):
    model = InstitucionCargoPersona

class PersonaAdmin(admin.ModelAdmin):
    inlines = [
        InstitucionPersonaInline,
    ]
    
admin.site.register(Persona, PersonaAdmin)

# <----  Admin site ---->
class ProtocoleInline(admin.TabularInline):
    model = Protocole


class RefujioInline(admin.TabularInline):
    model = Refujio

class CatastropheAdmin(admin.ModelAdmin):
    inlines = [ProtocoleInline, RefujioInline]

admin.site.register(Catastrophe, CatastropheAdmin)
admin.site.register(Protocole)
admin.site.register(Refujio)

