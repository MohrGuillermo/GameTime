from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts={k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Modificar Contraseña: ", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña: ", widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts={k:"" for k in fields}


class loginForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    def __str__(self):
        return f'Email: {self.email}, - Password: {self.password}'



class EventForm(forms.Form):
    nombre = forms.CharField(max_length=255)
    apellido = forms.CharField(max_length=255)
    fecha = forms.DateTimeField()
    descripcion = forms.CharField()
    ubicacion = forms.CharField(max_length=255)
