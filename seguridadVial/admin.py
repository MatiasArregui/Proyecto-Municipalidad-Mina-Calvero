from django.contrib import admin
from .models import Cargo, Elementos, Institucion, InstitucionCargoPersona, Persona
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
