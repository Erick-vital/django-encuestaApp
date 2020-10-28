from django.urls import path
from . import views

""" el url de 'detail' es un poco diferente
    a las demas vistas, solo es para variar
    un poco la forma de escribir los url
"""
app_name= 'encuesta'
urlpatterns = [ 
    # /encuesta/
    path('', views.IndexView.as_view(), name='index'),
    # /encuesta/id/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /encuesta/id/resultados/
    path('<int:pk>/resultados/', views.ResultadosView.as_view(), name='resultados'),
    # /encuesta/id/voto
    path('<int:pregunta_id>/voto', views.voto, name='voto'),
]

""" 'pregunta_id' es tomada de los parametros
    de las vistas(o vista)
"""
