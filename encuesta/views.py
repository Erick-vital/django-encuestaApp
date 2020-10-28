from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pregunta, Eleccion
#importa reverse
from django.urls import reverse
#import las vistas genericas
from django.views import generic


# Create your views here.
""" vistas basadas en clases, cada clase es una vista
    donde podemos agregar diferentes 'metodos' a cada clase
    en ves de tener todo nuestro codigo dentro de una funcion
"""

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'preguntas_set'

    def get_queryset(self):
        #devuleve el set, 'las preguntas del modelo'
        return Pregunta.objects.all()

class DetailView(generic.DetailView):
    model = Pregunta
    template_name = 'detail.html'

class ResultadosView(generic.DetailView):
    model = Pregunta
    template_name = 'resultados.html'

def voto(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        pregunta_actual = pregunta.eleccion_set.get(
            pk=request.POST['eleccion'])
    except  (KeyError, pregunta.DoesNotExist):
        return render(request, 'detail.html', {
            'pregunta':pregunta,
            'error_message': 'no seleccionaste una pregunta.',
        })

    else:
        pregunta_actual.votos += 1
        pregunta_actual.save()

        return HttpResponseRedirect(
            reverse('encuesta:resultados', args=(pregunta.id,)))

