from django.shortcuts import render
from django.shortcuts import render 
from django.urls import reverse_lazy 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from GameTimeApp.forms import UserRegistrationForm, UserEditForm
from GameTimeApp.models import Faq, Event, Game, Contact



def index(request):
    return render(request, 'index.html')


def us(request):
    return render(request, 'us.html')

class Contact(CreateView):
    model = Contact
    fields = ['nombre', 'email', 'mensaje']
    template_name = 'contact.html'
    success_url = reverse_lazy('index.html')


def galery(request):
    return render(request, 'galery.html')

def profile_edit(request):
    usuario = request.User
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:
            info = miFormulario.cleaned_data
            usuario.mail = info['email']
            usuario.password = info['password']
            usuario.password_2 = info['password_2']
            usuario.save()
        context = {f'mensaje':'Usuario: {usuario.nombre} editado con éxito'} 
        return render(request, 'index.html', context)
    else:
        miFormulario = UserEditForm(initial = {'email':usuario.email})
        context = {f'mensaje':'Usuario: {usuario.nombre} editado con éxito'}
    return render(request, 'profile_edit.html', {'miFormulario':miFormulario, 'usuario': usuario})

#Formulario de registro heredado de .forms que a su vez heredó a la clase de django 'UserCreationForm' y la modificó.
def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) #Aca determinamos el uso de 'nuestro' formulario. 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render(request, 'index.html', {'username': username})
        else:
            return render(request, 'register.html', {'form': form, 'error': 'El usuario ya existe o los datos ingresados son incorrectos'})
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

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
    template_name = 'eventList.html'
class EventDetail(DetailView):
    model = Event
    template_name = 'eventDetail.html'
class EventCreation(CreateView):
    model = Event
    fields = ['nombre', 'fecha', 'ubicacion', 'descripcion']
    template_name = 'eventForm.html'
    success_url = reverse_lazy('eventList.html')
class EventUpdate(UpdateView):
    model = Event
    fields = ['nombre', 'fecha', 'descripcion']
    template_name = 'eventForm.html'
    success_url = reverse_lazy('eventList.html')

class EventDelete(DeleteView):
    model = Event
    template_name = 'eventDelete.html'
    success_url = reverse_lazy('eventList.html')

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
    template_name = 'faqList.html'
class FaqDetail(DetailView):
    model = Faq
    template_name = 'FaqDetail.html'
class FaqCreation(CreateView):
    model = Faq
    fields = ['pregunta']
    template_name = 'faqForm.html'
    success_url = reverse_lazy('faqList.html')

class FaqAnswer(UpdateView):
    model = Faq
    fields = ['pregunta', 'respuesta']
    template_name = 'faqForm.html'
    success_url = reverse_lazy('faqList.html')

class FaqDelete(DeleteView):
    model = Faq
    template_name = 'faqDelete.html'
    success_url = reverse_lazy('faqList.html')
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

#games
class GameList(ListView):
    model = Game
    template_name = 'gameList.html'
class GameDetail(DetailView):
    model = Game
    template_name = 'gameDetail.html'

class GameCreation(CreateView):
    model = Game
    fields = ['nombre', 'descripcion']
    template_name = 'gameForm.html'
    success_url = reverse_lazy('gameList.html')

class GameUpdate(UpdateView):
    model = Game
    fields = ['nombre', 'descripcion']
    template_name = 'gameForm.html'
    success_url = reverse_lazy('gameList.html')

class GameDelete(DeleteView):
    model = Game
    template_name = 'gameDelete.html'
    success_url = reverse_lazy('gameList.html')