from django.contrib import admin
from .models import Cargo, Categoria, Elementos, Institucion, InstitucionPersona, Persona, InstitucionElemento
# Register your models here.
# INLINE DETALLE  ---------------------------->
class InstitucionPersonaInline(admin.TabularInline):
    model = InstitucionPersona


class InstitucionElementoInline(admin.TabularInline):
    model = InstitucionElemento

class InstitucionAdmin(admin.ModelAdmin):
    inlines = [
        InstitucionPersonaInline,
        InstitucionElementoInline,
    ]
     
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Cargo)
admin.site.register(Categoria)
admin.site.register(Elementos)
admin.site.register(Persona)