# Importamos el modelo User que vamos a heredar para crear nuestras cuentas de usuarios.
from django.contrib.auth.models import User

# Estas tres línes siguientes compensan el no poder hacer override sobre clases abstractas
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

# Definimos el modelo Usuario el cual utilizaremos para iniciar sesión, publicar post, editarlos, etc.
class Usuario(User):
    # no permite hacer override sobre clases abstractas, tales como AbstractUser
    #email = models.EmailField(unique=True)

    def __str__(self):
        return self.get_username()