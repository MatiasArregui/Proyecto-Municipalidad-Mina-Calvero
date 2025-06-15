from django.contrib import admin
from .models import Cargo, Elementos, Institucion, InstitucionPersona, Persona, CargoPersona
admin.site.register(Institucion)
admin.site.register(Cargo)
admin.site.register(Elementos)

# INLINE DETALLE  ---------------------------->
class InstitucionPersonaInline(admin.TabularInline):
    model = InstitucionPersona


class CargoPersonaInline(admin.TabularInline):
    model = CargoPersona

class PersonaAdmin(admin.ModelAdmin):
    inlines = [
        InstitucionPersonaInline,
        CargoPersonaInline,
    ]
    
admin.site.register(Persona, PersonaAdmin)
