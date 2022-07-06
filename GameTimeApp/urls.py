
from django.urls import path

# Vistas generales
from GameTimeApp.views import contacto, index, us, login_request, registro, buscarUsuario, UsuariosList, vistaSuperUser
from django.contrib.auth.views import LogoutView
from GameTimeApp.views import editarPerfil
# Vistas juegos
from GameTimeApp.views import toro, reloj, inflables
# Vistas FAq
from GameTimeApp.views import FaqList, FaqCreation

urlpatterns = [
    # Paths generales
    path('', index, name='index'),
    path('us/', us, name='us'),
    path('contacto/', contacto, name='contacto'),
    # Paths de logueo    
    path('registro/', registro, name='registro'),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='GameTimeApp/logout.html'), name='logout'),
    path('buscarUsuario/', buscarUsuario, name='buscarUsuario'),
    path('UsuariosList/', UsuariosList, name='UsuariosList'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('vistaSuperUser/', vistaSuperUser, name='vistaSuperUser'),
    #GAMES
    path('toro/', toro, name="toro"),
    path('reloj/', reloj, name="reloj"),
    path('inflables/', inflables, name="inflables"),
    #FAq'S
    path('faq_List/', FaqList.as_view(), name= 'faq_List'),
    path('faq/create/', FaqCreation.as_view(), name='faq_Create'),
    
]