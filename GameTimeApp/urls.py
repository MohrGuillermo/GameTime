
from django.urls import path

# Vistas generales
from GameTimeApp.views import index, us, login, registro, buscarUsuario, buscarUsuarioResultados, Contact
from django.contrib.auth.views import LogoutView
from GameTimeApp.views import profile_edit
# Vistas eventos
from GameTimeApp.views import EventList, EventCreation, EventUpdate, EventDelete, EventList, EventCreation, EventUpdate, EventDelete, buscarEvento, buscarEventoResultados, EventDetail
# Vistas juegos
from GameTimeApp.views import GameList, GameCreation, GameUpdate, GameDelete, GameList, GameCreation, GameUpdate, GameDelete
# Vistas FAq
from GameTimeApp.views import FaqList, FaqCreation, FaqAnswer, FaqDelete, buscarFaq, buscarFaqResultados, FaqDetail

urlpatterns = [
    # Paths generales
    path('', index, name='index'),
    path('us/', us, name='us'),
    path('contacto/', Contact.as_view(), name='contacto'),
    # Paths de logueo    
    path('registro/', registro, name='registro'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='GameTimeApp/logout.html'), name='logout'),
    path('buscarUsuario/', buscarUsuario, name='buscarUsuario'),
    path('buscarUsuarioResultados', buscarUsuarioResultados, name='buscarUsuarioResultados'),
    path('editarPerfil/', profile_edit, name='editarPerfil'),
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
    path('games/create/', GameCreation.as_view(), name='games_create'),
    path('games/update/<pk>/', GameUpdate.as_view(), name='games_update'),
    path('games/delete/<pk>/', GameDelete.as_view(), name='games_delete'),
    path('games/', GameList.as_view(), name='games'),
    #FAq'S
    path('faqList', FaqList.as_view(), name= 'faqList'),
    path('faq/create/', FaqCreation.as_view(), name='faq_create'),
    path('faq/update/<pk>/', FaqAnswer.as_view(), name='faq_update'),
    path('faq/delete/<pk>/', FaqDelete.as_view(), name='faq_delete'),
    path('faq/buscar/', buscarFaq, name='buscar_faq'),
    path('faq/buscar/resultados', buscarFaqResultados, name='buscar_faq_resultados'),
    
]