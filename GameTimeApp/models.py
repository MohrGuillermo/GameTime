from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Nombre: {self.nombre}, - Apellido: {self.apellido}, - Email: {self.email}, - Password: {self.password}'

class Faq(models.Model):
    pregunta = models.CharField(max_length=300)
    respuesta = models.CharField(max_length=300)
    

class Event(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Nombre: {self.nombre}, - Fecha: {self.fecha}, - Descripcion: {self.descripcion}'


class Game(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Nombre: {self.nombre}, - Descripcion: {self.descripcion}'


class User_event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'User: {self.user}, - Event: {self.event}, - Fecha: {self.fecha}' 


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(User_event)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'User: {self.user}, - Events: {self.events}'

