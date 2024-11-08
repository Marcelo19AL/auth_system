# predictions/urls.py
from django.urls import path
from .views import hacer_prediccion, lista_predicciones, lista_notificaciones, lista_partidos,agregar_partido
from . import views
urlpatterns = [
    path('hacer_prediccion/<int:partido_id>/', views.hacer_prediccion, name='hacer_prediccion'),
    path('lista_predicciones/', lista_predicciones, name='lista_predicciones'),
    path('mis_predicciones/', lista_predicciones, name='predicciones'),
    path('agregar_partido/', agregar_partido, name='agregar_partido'),  # Nueva ruta para agregar partidos
    path('lista_partidos/', lista_partidos, name='lista_partidos'),  # Nueva ruta para listar partidos
    path('notificaciones/', lista_notificaciones, name='notificaciones'),

]
