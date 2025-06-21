from django.contrib import admin
from .models import Cargo, Elementos, Institucion, InstitucionCargoPersona, Persona, Catastrophe, Protocole, Refujio, url_map
admin.site.register(Institucion)
admin.site.register(Cargo)
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

class UrlMapInline(admin.TabularInline):
    model = url_map

class CatastropheAdmin(admin.ModelAdmin):
    inlines = [ProtocoleInline, RefujioInline, UrlMapInline]

admin.site.register(Catastrophe, CatastropheAdmin)
admin.site.register(Protocole)
admin.site.register(Refujio)
admin.site.register(url_map)
