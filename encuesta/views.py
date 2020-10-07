from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pregunta, Eleccion

#importa reverse
from django.urls import reverse

# Create your views here.
def index(request):
    preguntas_set = Pregunta.objects.all()
    contexto = {'preguntas_set':preguntas_set}
    return render(request, 'index.html', contexto)


def detail(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    contexto = {'pregunta':pregunta}
    
    return render(request, 'detail.html', contexto)

def resultados(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)

    return render(request, 'resultados.html', {
        'pregunta':pregunta})

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
            reverse('resultados', args=(pregunta.id,)))

