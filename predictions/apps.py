from django.apps import AppConfig

class PredictionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predictions'

    def ready(self):
        from .models import Deporte
        # Verifica si ya existen los deportes antes de crear nuevos
        deportes = ['fútbol', 'tenis', 'baloncesto']
        for nombre in deportes:
            Deporte.objects.get_or_create(nombre=nombre)
