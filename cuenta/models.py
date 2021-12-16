# Importamos el modelo User que vamos a heredar para crear nuestras cuentas de usuarios.
from django.contrib.auth.models import User, Group
from django.db import models
#from django.conf import settings

#User = settings.AUTH_USER_MODEL


# Estas tres línes siguientes compensan el no poder hacer override sobre clases abstractas
# User._meta.get_field('email')._unique = True
# User._meta.get_field('email').blank = False
# User._meta.get_field('email').null = False

# Nos permitirá definir los tipos de usuarios en la web
# class TipoUsuario(models.Model):
#     descripcion = models.TextField(required=True, max_length=50, unique=True)

# Definimos el modelo Usuario el cual utilizaremos para iniciar sesión, publicar post, editarlos, etc.
class Usuario(User):#(models.Model): #
    # class Meta:
    #     proxy = True
    # no permite hacer override sobre clases abstractas, tales como AbstractUser
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #email = models.EmailField(unique=True)
    # tipo = models.ForeignKey(TipoUsuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.get_username()
    
    # Devuelve True si el usuario tiene privilegios de <Administrador>.
    @property
    def EsAdministrador(self):
        return self.groups.filter(name = 'Administrador').exists()
    
    # Devuelve True si el usuario tiene privilegios de <Escritor>.
    @property
    def EsEscritor(self):
        return True #self.groups.filter(natural_key='Escritor').exists()
    
    # Devuelve True si el usuario tiene privilegios de <Lector>.
    @property
    def EsLector(self):
        return self.groups.filter(name = 'Lector').exists()
