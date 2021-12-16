# Importamos RENDER y REDIRECT
from django.shortcuts import render, redirect

from cuenta.models import Usuario
from publicacion.models import Publicacion
from publicacion.forms import *

# Create your views here.

def index(request): # inicio de la página web
    listado = Publicacion.objects.all()
    template = 'publicacion/lista.html'
    contexto = {'publicaciones': listado, }

    return render(request, template, contexto)

def nosotros(request):
    template = 'nosotros.html'
    contexto = {}

    return render(request, template, contexto)

# Mostrará el form para crear una nueva publicación
def nueva(request):
    if request.method == 'POST':
        form = PublicacionNuevaForm(request.POST) # Instanciamos el modelo de FORM que definimos y le asignamos el parámetro <request.POST>
                                             # para que pase los datos que ingresamos para crear el nuevo usuario.
        if form.is_valid(): # verificamos si todos los datos ingresados (principalmente los requeridos, como nombre de usuario, 
                            # email, clave) están y son válidos.
            #form.autor = Usuario.objects.get(id=request.user.id) # Usuario.objects.get(request.user)
            # Sí entra aquí, quiere decir que están bien los datos
            form.save() # Asi que vamos a guardarlos (a registrar el usuario en al base de datos)
            
            return redirect('../') # retornamos una url que nos manda a cuenta/index.html (panel de opciones para el usuario)

    else: # Si el método pasado no es POST
        form = PublicacionNuevaForm() # mostramos el form vacío para que el cliente lo rellene

    contexto = {'form': form, } # definimos el contexto para usar en el archivo .html
    return render(request, 'publicacion/nueva.html', contexto) # renderizamos

def editar(request, id):
    pass

def eliminar(request, id):
    pass

def ver(request, id):
    pass