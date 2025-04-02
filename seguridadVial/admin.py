from django.contrib import admin
from .models import Cargo, Categoria, Elementos, Institucion, InstitucionPersona, Persona
# Register your models here.
# INLINE DETALLE DE ORDEN ---------------------------->
class InstitucionPersonaInline(admin.TabularInline):
    model = InstitucionPersona

class InstitucionAdmin(admin.ModelAdmin):
    inlines = [
        InstitucionPersonaInline,
    ]
     
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Cargo)
admin.site.register(Categoria)
admin.site.register(Elementos)
admin.site.register(Persona)