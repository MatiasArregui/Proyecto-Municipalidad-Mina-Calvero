from django.db import models

# Funcion de remplazo del set, les dejo el ejemplo
# def seleccionar_mesa_alternativa():
#     # Buscamos el mozo comun o base que remplazara a los demas
#     mesa_alternativa = Mesa.objects.filter(nombre__exact="Mesa predeterminada").first()
#     if mesa_alternativa:
#         return mesa_alternativa



# Create your models here.
class Elementos(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=120, default="", null=True, blank=True)
    # aca vamos a tener que poner un SET con un predeterminado
    # ej:  id_cliente = models.ForeignKey(Cliente, on_delete=models.SET(seleccionar_cliente_alternativo))
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    estado = models.BooleanField(default=False, null=True, blank=True)
    id_institucion = models.ForeignKey('Institucion', on_delete=models.CASCADE)
    id_persona = models.ForeignKey('Persona', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    
    def __str__(self):
        return self.nombre
    
class Institucion(models.Model):
    nombre = models.CharField(max_length=120, null=True, blank=True)
    mail = models.CharField(max_length=120, default="", null=True, blank=True)
    descripcion = models.CharField(max_length=120, default="", null=True, blank=True)
    direccion = models.CharField(max_length=120, default="", null=True, blank=True)
    telefono = models.CharField(max_length=30, default="",null=True, blank=True)
    id_persona = models.ManyToManyField('Persona', through='InstitucionPersona')
    
    def __str__(self):
        return self.nombre

class InstitucionPersona(models.Model):
    id_persona = models.ForeignKey('persona', on_delete=models.CASCADE)
    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)


class Persona(models.Model):
    nombre = models.CharField(max_length=120)
    dni = models.IntegerField(default=0)
    telefono = models.CharField(max_length=30, default="",null=True, blank=True)
    # aca vamos a tener que poner un SET con un predeterminado
    # ej:  id_cliente = models.ForeignKey(Cliente, on_delete=models.SET(seleccionar_cliente_alternativo))
    id_cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Cargo(models.Model):
    nombre = models.CharField(max_length=120)
    
    def __str__(self):
        return self.nombre

