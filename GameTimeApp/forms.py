from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')


class UserEvent(forms.Form):
    nombre = forms.CharField(max_length=255)
    fecha = forms.DateTimeField()
    descripcion = forms.TextField()
    created_at = forms.DateTimeField(auto_now_add=True)
    updated_at = forms.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Nombre: {self.nombre}, - Fecha: {self.fecha}, - Descripcion: {self.descripcion}'












# class UserForm(forms.Form):
#     nombre = forms.CharField(max_length=255)
#     apellido = forms.CharField(max_length=255)
#     email = forms.CharField(max_length=255)
#     password = forms.CharField(max_length=255)
#     created_at = forms.DateTimeField(auto_now_add=True)
#     updated_at = forms.DateTimeField(auto_now=True)
#     def __str__(self):
#         return f'Nombre: {self.nombre}, - Apellido: {self.apellido}, - Email: {self.email}, - Password: {self.password}'



# class loginForm(forms.Form):
#     email = forms.CharField(max_length=255)
#     password = forms.CharField(max_length=255)
#     def __str__(self):
#         return f'Email: {self.email}, - Password: {self.password}'


# class RegisterForm(forms.Form):
#     nombre = forms.CharField(max_length=255)
#     apellido = forms.CharField(max_length=255)
#     email = forms.CharField(max_length=255)
#     password = forms.CharField(max_length=255)
#     created_at = forms.DateTimeField(auto_now_add=True)
#     updated_at = forms.DateTimeField(auto_now=True)
#     def __str__(self):
#         return f'Nombre: {self.nombre}, - Apellido: {self.apellido}, - Email: {self.email}, - Password: {self.password}'


# class ContactForm(forms.Form):
#     nombre = forms.CharField(max_length=255)
#     email = forms.CharField(max_length=255)
#     mensaje = forms.TextField()
#     created_at = forms.DateTimeField(auto_now_add=True)
#     updated_at = forms.DateTimeField(auto_now=True)
#     def __str__(self):
#         return f'Nombre: {self.nombre}, - Email: {self.email}, - Mensaje: {self.mensaje}'