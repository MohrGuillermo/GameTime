from django.shortcuts import redirect, render
from django.shortcuts import render 
from django.urls import reverse_lazy 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Faq, Event, Game, User



def index(request):
    return render(request, 'index.html')


def us(request):
    return render(request, 'us.html')

def contact(request):
    return render(request, 'contact.html')


def galery(request):
    return render(request, 'galery.html')
    
def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html') 


def profile(request):
    return render(request, 'profile.html')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render(request, 'index.html', {'username': username})
        else:
            return render(request, 'register.html', {'form': form, 'error': 'El usuario ya existe o los datos ingresados son incorrectos'})
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {'username': username})
            else:
                return render(request, 'login.html', {'form': form, 'error': 'El usuario o la contraseña son incorrectos'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Error en la validacion de datos'})

def buscarUsuario(request):
    return render(request, 'buscarUsuario.html')

def buscarUsuarioResultados(request):
    if request.GET == 'POST':
        nombre = request.POST['nombre']
        usuarios = User.objects.filter(username=nombre)
        return render(request, 'buscarUsuarioResultados.html', {'usuarios': usuarios}, {'nombre': nombre})
    else:
        return render(request, 'buscarUsuario.html', {'error': 'No hay usuarios con ese nombre'})



# Events
class EventList(ListView):
    model = Event
    template_name = 'events.html'
class EventCreation(CreateView):
    model = Event
    fields = ['nombre', 'fecha', 'descripcion']
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')
class EventUpdate(UpdateView):
    model = Event
    fields = ['nombre', 'fecha', 'descripcion']
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')
class EventDelete(DeleteView):
    model = Event
    template_name = 'event_delete.html'
    success_url = reverse_lazy('event_list')
def buscarEvento(request):
    return render(request, 'buscarEvento.html')
def buscarEventoResultados(request):
    if request.GET == 'POST':
        fecha = request.POST['fecha']
        eventos = Event.objects.filter(fecha=fecha)
        return render(request, 'buscarEventoResultados.html', {'eventos': eventos}, {'fecha': fecha})
    else:
        return render(request, 'buscarEvento.html', {'error': 'No hay eventos programados en esa fecha'})

#FAQ
class FaqList(ListView):
    model = Faq
    template_name = 'faqlist.html'
class FaqCreation(CreateView):
    model = Faq
    fields = ['pregunta', 'respuesta']
    template_name = 'faq_form.html'
    success_url = reverse_lazy('faq_list')
class FaqUpdate(UpdateView):
    model = Faq
    fields = ['pregunta', 'respuesta']
    template_name = 'faq_form.html'
    success_url = reverse_lazy('faq_list')
class FaqDelete(DeleteView):
    model = Faq
    template_name = 'faq_delete.html'
    success_url = reverse_lazy('faq_list')
def buscarFaq(request):
    return render(request, 'buscarFaq.html')
def buscarFaqResultados(request):
    if request.GET == 'POST':
        palabra = request.POST['palabra']
        pregunta = Faq.objects.all().filter(pregunta__contains=palabra)
        if pregunta is not None:
                return render(request, 'buscarFaqResultados.html', {'palabra': palabra, 'pregunta': pregunta})
        else:
            return render(request, 'buscarFaqResultados.html', {'error': 'No hay preguntas que coinicidan con esa palabra clave'})


class GameList(ListView):
    model = Game
    template_name = 'games.html'
class GameCreation(CreateView):
    model = Game
    fields = ['nombre', 'descripcion']
    template_name = 'game_form.html'
    success_url = reverse_lazy('game_list')
class GameUpdate(UpdateView):
    model = Game
    fields = ['nombre', 'descripcion']
    template_name = 'game_form.html'
    success_url = reverse_lazy('game_list')
class GameDelete(DeleteView):
    model = Game
    template_name = 'game_delete.html'
    success_url = reverse_lazy('game_list')





