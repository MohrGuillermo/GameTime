
from django.urls import path
# Vistas generales
from .views import  index, us, login, registro, login, buscarUsuario, buscarUsuarioResultados
from django.contrib.auth.views import LogoutView
# Vistas eventos
from .views import EventList, EventCreation, EventUpdate, EventDelete, EventList, EventCreation, EventUpdate, EventDelete, buscarEvento, buscarEventoResultados
# Vistas juegos
from .views import GameList, GameCreation, GameUpdate, GameDelete, GameList, GameCreation, GameUpdate, GameDelete
# Vistas FAq
from .views import FaqList, FaqCreation, FaqUpdate, FaqDelete, FaqList, FaqCreation, FaqUpdate, FaqDelete, buscarFaq, buscarFaqResultados


urlpatterns = [
    # Paths generales
    path('index/', index, name='index'),
    path('us/', us, name='us'),
    # Paths de logueo    
    path('registro/', registro, name='registro'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='GameTimeApp/logout.html'), name='logout'),
    path('buscarUsuario/', buscarUsuario, name='buscarUsuario'),
    path('buscarUsuarioResultados', buscarUsuarioResultados, name='buscarUsuarioResultados'),
    #EVENTS
    path('events/create/', EventCreation.as_view(), name='events_create'),
    path('events/update/<pk>/', EventUpdate.as_view(), name='events_update'),
    path('events/delete/<pk>/', EventDelete.as_view(), name='events_delete'),
    path('events/', EventList.as_view(), name='eventos'),
    path('events/buscar/', buscarEvento, name='buscar_eventos'),
    path('events/buscar/resultados', buscarEventoResultados, name='buscar_eventos_resultados'),
    #GAMES
    path('games/create/', GameCreation.as_view(), name='games_create'),
    path('games/update/<pk>/', GameUpdate.as_view(), name='games_update'),
    path('games/delete/<pk>/', GameDelete.as_view(), name='games_delete'),
    path('games/', GameList.as_view(), name='games'),
    #FAq'S
    path('faq/create/', FaqCreation.as_view(), name='faq_create'),
    path('faq/update/<pk>/', FaqUpdate.as_view(), name='faq_update'),
    path('faq/delete/<pk>/', FaqDelete.as_view(), name='faq_delete'),
    path('faq/', FaqList.as_view(), name='faq'),
    path('faq/buscar/', buscarFaq, name='buscar_faq'),
    path('faq/buscar/resultados', buscarFaqResultados, name='buscar_faq_resultados'),
    
]