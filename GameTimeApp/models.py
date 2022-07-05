from django.db import models
from django.contrib.auth.models import User 

class Faq(models.Model):
    pregunta = models.CharField(max_length=300)
    respuesta = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.pregunta} {self.respuesta}' 


class Event(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha = models.CharField(max_length=255)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    def __str__(self):
        return f'Nombre completo: {self.nombre, self.apellido}, - Fecha: {self.fecha}, - Ubicacion: {self.ubicacion}'


class Game(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Nombre: {self.nombre}, - Descripcion: {self.descripcion}'

class Contact(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    mensaje = models.CharField(max_length=255)
    def __str__(self):
        return f'Nombre: {self.nombre}, - Email: {self.email}, - Mensaje: {self.mensaje}'