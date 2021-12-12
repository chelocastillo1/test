from django.db import models
from cuenta.models import Usuario
from django.db.models.deletion import SET_NULL

class Publicacion (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaEdicion = models.DateTimeField(auto_now=True)