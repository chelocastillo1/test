# Importamos los formularios predefinidos que ya trae Django
from django import forms

# Importamos el modelo Usuario que creamos
from cuenta.models import Usuario

# Importamos formularios predefinidos de Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from django.core.exceptions import ValidationError

# Definimos la clase que mostrará los campos que queremos rellenar al momento de registra un nuevo usuario
class CuentaNuevaForm(UserCreationForm): # Que tiene como clase base <UserCreationForm>
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario # Que tome como modelo la clase <Usuario> que creamos y heredamos de <User>

        # FIELDS permite especificar los campos a mostrar, pero a su vez, 
        # nos ahorra el trabajo de tener que espeficicar si es numerico, texto, etc., entre otras cosas
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', ) # Definimos campos a mostrar en el form de registro
        widgets = {'password': forms.PasswordInput(), 'email': forms.EmailInput(), } # define el tipo de entrada, y además añade verificación
                                                                                     # por ejemplo el campo email, lo valida al momento de enviar el form

# Definimos la clase que mostrará el formulario de inicio de sesión (login)
class IniciarSesionForm(AuthenticationForm): # heredado de AuthenticationForm
    class Meta:
         model = Usuario # modelo
         fields = ['username', 'password'] # campos
         widgets = {'password': forms.PasswordInput(), }

    def confirm_login_allowed(self, user): # no sé cómo hacer para que "pase" por aquí
        if not user.is_active:
            raise forms.ValidationError('Esta cuenta está deshabilitada por el administrador.', code='inactive', )

# Definición de la clase form para el cambio de contraseña
class CambiarPasswordForm(PasswordChangeForm):
    pass

# class CambiarEmailForm(EmailChangeForm):
#     pass