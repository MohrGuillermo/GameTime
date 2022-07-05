
from django.urls import path

# Vistas generales
from GameTimeApp.views import contacto, index, us, login_request, registro, buscarUsuario, buscarUsuarioResultados
from django.contrib.auth.views import LogoutView
from GameTimeApp.views import editarPerfil
# Vistas eventos
from GameTimeApp.views import EventList, EventCreation, EventUpdate, EventDelete, EventList, EventCreation, EventUpdate, EventDelete, buscarEvento, buscarEventoResultados, EventDetail
# Vistas juegos
from GameTimeApp.views import toro, reloj, inflables
# Vistas FAq
from GameTimeApp.views import FaqList, FaqCreation, FaqAnswer, FaqDelete

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
    path('buscarUsuarioResultados', buscarUsuarioResultados, name='buscarUsuarioResultados'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    #EVENTS
    path('events/create/', EventCreation.as_view(), name='events_create'),
    path('events/update/<pk>/', EventUpdate.as_view(), name='events_update'),
    path('events/delete/<pk>/', EventDelete.as_view(), name='events_delete'),
    path('events/', EventList.as_view(), name='eventos'),
    path('events/buscar/', buscarEvento, name='buscar_eventos'),
    path('events/buscar/resultados', buscarEventoResultados, name='buscar_eventos_resultados'),
    path('eventDetail', EventDetail.as_view(), name= 'EventDetail'),
    
    path('eventDetail', EventDetail.as_view(), name= 'EventDetail'),
    path('eventDetail', EventDetail.as_view(), name= 'EventDetail'),
    #GAMES
    path('toro/', toro, name="toro"),
    path('reloj/', reloj, name="reloj"),
    path('inflables/', inflables, name="inflables"),
    #FAq'S
    path('faqList/', FaqList.as_view(), name= 'faqList'),
    path('faq/create/', FaqCreation.as_view(), name='faq_create'),
    path('faq/update/<pk>/', FaqAnswer.as_view(), name='faq_update'),
    path('faq/delete/<pk>/', FaqDelete.as_view(), name='faq_delete'),
    # path('buscarFaqResultados/', buscarFaqResultados, name='buscarFaqResultados'),
    
]