from django.db import models
from cuenta.models import Usuario
#from cuenta.models import *

class Publicacion(models.Model):
    # Definición de claves foráneas
    autor = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, default=0)
    #comentario = models.ForeignKey(Comentario, on_delete=models.DO_NOTHING)
    #voto = models.ForeignKey(Voto, on_delete=models.DO_NOTHING) # Like

    # Definición de los campos/atributos
    #id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False) #blank determina que si o si se escriba algo
    contenido = models.TextField(blank=False)
    destacado = models.BooleanField(default=False)
    imagen = models.ImageField(blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True) # auto_created=True # 
    fechaEdicion = models.DateTimeField(auto_now=True) # editable=False # 

    # Definición de propiedades y métodos
    def __str__(self):
        return self.titulo
    
    @property
    def Id(self):
        return self.id

# class Comentario(models.Model):
#     publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
#     email = models.EmailField()

#     contenido = models.TextField()
#     fechaCreacion = models.DateTimeField()#auto_now_add=True
#     fechaEdicion = models.DateTimeField()#auto_now=True

# class Voto(models.Model):
#      usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
#      publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
