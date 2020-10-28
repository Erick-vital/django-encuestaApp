from django.test import TestCase
# Create your tests here.
import datetime
from django.utils import timezone
from .models import Pregunta



class PreguntaMoldelTests(TestCase):

    def test_fue_publicado_recientemente(self):
        """
        este metodo debe retornar falso si una fecha
        de publicacion es en el futuro
        """
        time = timezone.now().date() + datetime.timedelta(days=30)
        pregunta_futura = Pregunta(fecha_publicacion=time)
        self.assertIs(pregunta_futura.fue_publicado_recientemente(), False)
        

