from cmath import inf
from django.http import HttpResponse
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

from django.core.mail import send_mail
from django.conf import settings

def index(request):

    return render(request, 'GameTimeApp/index.html')


def us(request):
    return render(request, 'GameTimeApp/us.html')

def contacto(request):
    if request.method == 'POST':
        subject = request.POST["asunto"]
        message= request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['gteventos10@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'GameTimeApp/gracias.html')
    return render(request, 'GameTimeApp/contact.html')



def galery(request):
    return render(request, 'GameTimeApp/galery.html')

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, 'GameTimeApp/index.html', {'usuario': usuario, 'mensaje':'Datos cambiados exitosamente '})
    else:
            formulario = UserEditForm(instance=usuario)
    return render(request, 'GameTimeApp/editarPerfil.html', {'formulario': formulario, 'usuario': usuario.username})

#Formulario de registro heredado de .forms que a su vez heredó a la clase de django 'UserCreationForm' y la modificó.
def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) #Aca determinamos el uso de 'nuestro' formulario. 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render(request, 'GameTimeApp/register.html', {'mensaje': f'Usuario creado: {username}'})
        else:
            return render(request, 'GameTimeApp/register.html', {'form': form, 'mensaje': 'El usuario ya existe o los datos ingresados son incorrectos'})
    else:
        form = UserRegistrationForm()
    return render(request, 'GameTimeApp/register.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, 'GameTimeApp/index.html', {'mensaje': f'Bienvenido : {usuario}'})
            else:
                return render(request,"GameTimeApp/login.html", {'mensaje': 'Datos incorrectos'})
        else:
            return render(request, 'GameTimeApp/login.html', {'form': form, 'mensaje': 'Formulario erroneo'})
    form = AuthenticationForm()
    return render(request,"GameTimeApp/login.html",{'form':form})


def buscarUsuario(request):
    return render(request, 'GameTimeApp/buscarUsuario.html')


def buscarUsuarioResultados(request):
    if request.GET == 'POST':
        nombre = request.POST['nombre']
        usuarios = User.objects.filter(username=nombre)
        return render(request, 'GameTimeApp/buscarUsuarioResultados.html', {'usuarios': usuarios}, {'nombre': nombre})
    else:
        return render(request, 'GameTimeApp/buscarUsuario.html', {'error': 'No hay usuarios con ese nombre'})



# Events
class EventList(ListView):
    model = Event
    template_name = 'GameTimeApp/eventList.html'
class EventDetail(DetailView):
    model = Event
    template_name = 'GameTimeApp/eventDetail.html'
class EventCreation(CreateView):
    model = Event
    fields = ['nombre', 'fecha', 'ubicacion', 'descripcion']
    template_name = 'GameTimeApp/eventForm.html'
    success_url = reverse_lazy('GameTimeApp/eventList.html')
class EventUpdate(UpdateView):
    model = Event
    fields = ['nombre', 'fecha', 'descripcion']
    template_name = 'GameTimeApp/eventForm.html'
    success_url = reverse_lazy('GameTimeApp/eventList.html')

class EventDelete(DeleteView):
    model = Event
    template_name = 'GameTimeApp/eventDelete.html'
    success_url = reverse_lazy('GameTimeApp/eventList.html')

def buscarEvento(request):
    return render(request, 'GameTimeApp/buscarEvento.html')

def buscarEventoResultados(request):
    if request.GET == 'POST':
        fecha = request.POST['fecha']
        eventos = Event.objects.filter(fecha=fecha)
        return render(request, 'GameTimeApp/buscarEventoResultados.html', {'eventos': eventos}, {'fecha': fecha})
    else:
        return render(request, 'GameTimeApp/buscarEvento.html', {'error': 'No hay eventos programados en esa fecha'})

#FAQ
class FaqList(ListView):
    model = Faq
    template_name = 'GameTimeApp/faqList.html'

class FaqCreation(CreateView):
    model = Faq
    fields = ['pregunta', 'respuesta']
    template_name = 'GameTimeApp/faqForm.html'
    success_url = reverse_lazy('faqList')

class FaqAnswer(UpdateView):
    model = Faq
    fields = ['pregunta', 'respuesta']
    template_name = 'GameTimeApp/faqForm.html'
    success_url = reverse_lazy('GameTimeApp/faqList.html')

class FaqDelete(DeleteView):
    model = Faq
    template_name = 'GameTimeApp/faqDelete.html'
    success_url = reverse_lazy('GameTimeApp/faqList.html')
    

#games
def toro(request):
    return render (request, 'GameTimeApp/toro.html')
def reloj(request):
    return render(request, 'GameTimeApp/reloj.html')
def inflables(request):
    return render(request, 'GameTimeApp/inflables.html')