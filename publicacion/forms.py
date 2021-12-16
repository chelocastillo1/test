# Importamos los formularios predefinidos que ya trae Django
from django import forms
from django.forms import models

# Importamos el modelo Usuario que creamos
from publicacion.models import Publicacion

# Definimos la clase que mostrará los campos que queremos rellenar al momento de crear una publicación
class PublicacionNuevaForm(models.ModelForm):
    titulo = forms.CharField(max_length=100, required=True, label='Título') # , help_text='Defina el título para el artículo que desea publicar.'
    contenido = forms.CharField(label='Contenido') # help_text='Escriba el texto para el artículo.'
    destacado = forms.BooleanField(required=False)
    imagen = forms.ImageField(required=False, label='Foto / imágen', help_text='Tamaño máximo de 850 x 350 pixeles.') # , help_text='Suba una foto/imágen que aparecerá e identificará a la publicación.'
    #fechaCreacion = forms.DateTimeField(label='Fecha de creación')
    #fechaEdicion = forms.DateTimeField(label='Fecha de útlima edición')

    class Meta:
        model = Publicacion # Que tome como modelo la clase <Publicacion> que creamos

        # FIELDS permite especificar los campos a mostrar, pero a su vez, 
        # nos ahorra el trabajo de tener que espeficicar si es numerico, texto, etc., entre otras cosas
        fields = ('titulo', 'contenido', 'destacado', 'autor') # Definimos campos a mostrar en el form de registro
