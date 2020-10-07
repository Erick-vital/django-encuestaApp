from django.urls import path
from . import views

""" el url de 'detail' es un poco diferente
    a las demas vistas, solo es para variar
    un poco la forma de escribir los url
"""

urlpatterns = [ 
    # /encuesta/
    path('', views.index, name='index'),
    # /encuesta/id/
    path('<int:pregunta_id>/', views.detail, name='detail'),
    # /encuesta/id/resultados/
    path('<int:pregunta_id>/resultados/', views.resultados, name='resultados'),
    # /encuesta/id/voto
    path('<int:pregunta_id>/voto', views.voto, name='voto' ),
]

""" 'pregunta_id' es tomada de los parametros
    de las vistas(o vista)
"""
