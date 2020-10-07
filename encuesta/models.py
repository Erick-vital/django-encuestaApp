from django.db import models

# Create your models here.
""" un modelo es la mayor fuenta de
    verdad de tus datos

    para referencias visita:
    https://docs.djangoproject.com/en/3.0/ref/models/fields/
"""

#cada clase representa un modelo

class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()

    # metodo 'str', devulve una respuesta en texto 
    def __str__(self):
        texto = '\n pregunta: %s \n fecha de publicacion: %s \n'
        datos_pregunta = texto %(
            self.texto_pregunta, self.fecha_publicacion)
        return datos_pregunta

class Eleccion(models.Model):
    """ con el metodo 'foreignkey' estamos
        relacionando cada eleccion con una pregunta.

        esto es lo que llamamos un related object, para mas
        informacions sobre los related objects visita
        https://docs.djangoproject.com/en/3.0/ref/models/relations/
        https://docs.djangoproject.com/en/3.0/topics/db/examples/
    """
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    eleccion_texto = models.CharField(max_length=50)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.eleccion_texto


