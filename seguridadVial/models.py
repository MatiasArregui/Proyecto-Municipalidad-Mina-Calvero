from django.db import models



# Create your models here.
class Elementos(models.Model):
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=120, null=True, blank=True)
    descripcion = models.CharField(max_length=120, default="", null=True, blank=True)
    cantidad = models.IntegerField(default=1, null=True, blank=True)
    observaciones = models.CharField(max_length=240, null=True, blank=True)
    estado = models.BooleanField(default=True, null=True, blank=True)
    id_persona = models.ForeignKey("Persona", on_delete=models.PROTECT)
    id_institucion = models.ForeignKey("Institucion", on_delete=models.CASCADE)

    
    def __str__(self):
        return self.nombre
    
    def get_tipo(self):
        return "Elemento"
    
    
class Institucion(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=240)
    direccion = models.CharField(max_length=120, default="", null=True, blank=True)
    email = models.CharField(max_length=120, default="", null=True, blank=True)
    telefono = models.CharField(max_length=30, default="",null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    def get_tipo(self):
        return "Institucion"


# class Institucion(models.Model):
#     nombre = models.CharField(max_length=120, null=True, blank=True)
#     mail = models.CharField(max_length=120, default="", null=True, blank=True)
#     descripcion = models.CharField(max_length=120, default="", null=True, blank=True)
#     direccion = models.CharField(max_length=120, default="", null=True, blank=True)
#     telefono = models.CharField(max_length=30, default="", null=True, blank=True)
#     id_elementos = models.ManyToManyField(Elementos, through="InstitucionElemento")
#     # Campo para seleccionar una sola persona (representante)
#     id_persona_encargado = models.ForeignKey(
#         'Persona',
#         on_delete=models.SET(seleccionar_persona_remplazo),
#         related_name='encargado'
#     )
    
#     # Campo para seleccionar muchas personas
#     id_persona = models.ManyToManyField(
#         'Persona',
#         related_name='trabajadores'
#     )
    
#     def __str__(self):
#         return self.nombre
    
#     def get_tipo(self):
#         return "Institucion"


class Persona(models.Model):
    nombre_apellido = models.CharField(max_length=120)
    dni = models.IntegerField(default=0)
    telefono = models.CharField(max_length=30, default="",null=True, blank=True)
    id_institucion = models.ManyToManyField('Institucion', through="InstitucionCargoPersona")
    
    # aca vamos a tener que poner un SET con un predeterminado
    # ej:  id_cliente = models.ForeignKey(Cliente, on_delete=models.SET(seleccionar_cliente_alternativo))
    
    def __str__(self):
        return self.nombre_apellido
    
    def get_tipo(self):
        return "Persona"

    
class InstitucionCargoPersona(models.Model):
    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=120)



# class catastrofe(models.Model):
#     nombre = models.CharField(max_length=120)
#     latitud = models.FloatField()
#     longitud = models.FloatField()

#     def __str__(self):
#         return self.nombre




# <------------  Modelos Landing page   --------------->
class Catastrophe(models.Model):
    type_disaster = models.CharField(max_length=255, default=None)
    descripcion = models.TextField()
    is_active = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    image_disaster = models.CharField(max_length=255)
    mapa_interactivo = models.CharField(max_length=855, default=None)




    def __str__(self):
        return self.type_disaster



class Protocole(models.Model):
    CHOICE = [
        ('Antes', 'Antes'),
        ('Durante', 'Durante'),
        ('Despues', 'Despues')
    ]
    
    campo_seleccion = models.CharField(max_length=50, choices=CHOICE, default=None, null=True, blank=True)
    name = models.CharField(max_length=255, default=None, null=True, blank=True)
    catastrophe = models.ForeignKey(Catastrophe, on_delete=models.CASCADE, related_name="protocoles")

    def __str__(self):
        return self.name


class PdfFrame(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    pk_catastrofe = models.ManyToManyField(Catastrophe,through="CatPdf")

    def __str__(self):
        return f"Pdf de :{self.name}"
    
class CatPdf(models.Model):
    id_cat = models.ForeignKey(Catastrophe, on_delete=models.CASCADE)
    id_pdf = models.ForeignKey(PdfFrame, on_delete=models.CASCADE)
        
class Refujio(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    catastrofe = models.ForeignKey(Catastrophe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Refugio de {self.institucion.telefono} en caso de {self.catastrofe}"

# -------- Nuevas Tablas --------

class SubCatastrofe(models.Model):
    titulo = models.CharField(max_length=255, default=None)
    id_catastrofe = models.ForeignKey(Catastrophe, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Prevencion(models.Model):
    subcatastrofe = models.ForeignKey(SubCatastrofe, on_delete=models.CASCADE, related_name='prevenciones')
    titulo = models.CharField(max_length=255, default=None)
    descripcion = models.TextField(default=None)

    def __str__(self):
        return self.titulo

class Protocolo(models.Model):
    CHOICE = [
        ('Antes', 'Antes'),
        ('Durante', 'Durante'),
        ('Despues', 'Despues')
    ]

    subcatastrofe = models.ForeignKey(SubCatastrofe, on_delete=models.CASCADE, related_name='protocolos')
    tipo = models.CharField(max_length=50, choices=CHOICE, default=None, null=True, blank=True)
    descripcion = models.CharField(max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo}: {self.descripcion}"
# -------- 

# Tabla para manejar quienes integran la defensa civil

class IntegrantesDC(models.Model):
    titulo = models.CharField(max_length=255)
    persona = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    
    def __str__(self):
        return self.titulo