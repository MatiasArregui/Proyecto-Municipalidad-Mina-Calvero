from django.db import models

# Funcion de remplazo del set, les dejo el ejemplo
def seleccionar_categoria_remplazo():
    # Buscamos el mozo comun o base que remplazara a los demas
    categoria_alternativa = Categoria.objects.filter(nombre__exact="seleccionar categoria").first()
    if categoria_alternativa:
        return categoria_alternativa
def seleccionar_persona_remplazo():
    # Buscamos el mozo comun o base que remplazara a los demas
    persona_alternativa = Persona.objects.filter(nombre__exact="seleccionar persona").first()
    if persona_alternativa:
        return persona_alternativa
def seleccionar_cargo_remplazo():
    # Buscamos el mozo comun o base que remplazara a los demas
    cargo_alternativo = Cargo.objects.filter(nombre__exact="selecccionar cargo").first()
    if cargo_alternativo:
        return cargo_alternativo



# Create your models here.
class Elementos(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=120, default="", null=True, blank=True)
    cantidad = models.IntegerField(default=1, null=True, blank=True)
    # aca vamos a tener que poner un SET con un predeterminado
    # ej:  id_cliente = models.ForeignKey(Cliente, on_delete=models.SET(seleccionar_cliente_alternativo))
    id_categoria = models.ForeignKey('Categoria', on_delete=models.SET(seleccionar_categoria_remplazo))
    estado = models.BooleanField(default=False, null=True, blank=True)
    id_persona = models.ForeignKey('Persona', on_delete=models.SET(seleccionar_persona_remplazo))
    
    def __str__(self):
        return self.nombre
    
    def get_tipo(self):
        return "Elemento"

class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    
    def __str__(self):
        return self.nombre
    
    
    
# class Institucion(models.Model):
#     nombre = models.CharField(max_length=120, null=True, blank=True)
#     mail = models.CharField(max_length=120, default="", null=True, blank=True)
#     descripcion = models.CharField(max_length=120, default="", null=True, blank=True)
#     direccion = models.CharField(max_length=120, default="", null=True, blank=True)
#     telefono = models.CharField(max_length=30, default="",null=True, blank=True)
#     id_persona_encargado = models.ForeignKey('Persona', on_delete=models.CASCADE)
#     id_persona = models.ManyToManyField('Persona', through='InstitucionPersona')
    
#     def __str__(self):
#         return self.nombre


class Institucion(models.Model):
    nombre = models.CharField(max_length=120, null=True, blank=True)
    mail = models.CharField(max_length=120, default="", null=True, blank=True)
    descripcion = models.CharField(max_length=120, default="", null=True, blank=True)
    direccion = models.CharField(max_length=120, default="", null=True, blank=True)
    telefono = models.CharField(max_length=30, default="", null=True, blank=True)
    id_elementos = models.ManyToManyField(Elementos, through="InstitucionElemento")
    # Campo para seleccionar una sola persona (representante)
    id_persona_encargado = models.ForeignKey(
        'Persona',
        on_delete=models.SET(seleccionar_persona_remplazo),
        related_name='encargado'
    )
    
    # Campo para seleccionar muchas personas
    id_persona = models.ManyToManyField(
        'Persona',
        related_name='trabajadores'
    )
    
    def __str__(self):
        return self.nombre
    
    def get_tipo(self):
        return "Institucion"


class InstitucionPersona(models.Model):
    id_persona = models.ForeignKey('persona', on_delete=models.CASCADE)
    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    
class InstitucionElemento(models.Model):
    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    id_elemento = models.ForeignKey(Elementos, on_delete=models.CASCADE)


class Persona(models.Model):
    nombre = models.CharField(max_length=120)
    dni = models.IntegerField(default=0)
    telefono = models.CharField(max_length=30, default="",null=True, blank=True)
    # aca vamos a tener que poner un SET con un predeterminado
    # ej:  id_cliente = models.ForeignKey(Cliente, on_delete=models.SET(seleccionar_cliente_alternativo))
    id_cargo = models.ForeignKey('Cargo', on_delete=models.SET(seleccionar_cargo_remplazo))
    
    def __str__(self):
        return self.nombre
    
    def get_tipo(self):
        return "Persona"

class Cargo(models.Model):
    nombre = models.CharField(max_length=120)
    
    def __str__(self):
        return self.nombre


class catastrofe(models.Model):
    nombre = models.CharField(max_length=120)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return self.nombre

