from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts={k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(label="Modificar Contraseña: ", widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Confirmar contraseña: ", widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['email', 'password', 'password_2']
        help_texts={k:"" for k in fields}


class loginForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    def __str__(self):
        return f'Email: {self.email}, - Password: {self.password}'




# class UserEvent(forms.Form):
#     nombre = forms.CharField(max_length=255)
#     fecha = forms.DateTimeField()
#     descripcion = forms.TextField()
#     created_at = forms.DateTimeField(auto_now_add=True)
#     updated_at = forms.DateTimeField(auto_now=True)
#     def __str__(self):
#         return f'Nombre: {self.nombre}, - Fecha: {self.fecha}, - Descripcion: {self.descripcion}'


# class UserForm(forms.Form):
#     nombre = forms.CharField(max_length=255)
#     apellido = forms.CharField(max_length=255)
#     email = forms.CharField(max_length=255)
#     password = forms.CharField(max_length=255)
#     created_at = forms.DateTimeField(auto_now_add=True)
#     updated_at = forms.DateTimeField(auto_now=True)
#     def __str__(self):
#         return f'Nombre: {self.nombre}, - Apellido: {self.apellido}, - Email: {self.email}, - Password: {self.password}'


# class UserRegisterForm(forms.Form):
#     # nombre = forms.CharField(max_length=255)
#     # apellido = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     password = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
#     password_2 = forms.CharField(label = 'Repetir contraseña', widget = forms.PasswordInput)
#     # created_at = forms.DateTimeField(auto_now_add=True)
#     # updated_at = forms.DateTimeField(auto_now=True)
#     class Meta:
#         model = User
#         fields = ['username','email','password','password_2']
#         help_texts = {k:"" for k in fields}

