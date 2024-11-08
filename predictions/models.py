# predictions/models.py
from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='fotos_perfil', blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)  # Biografía del usuario
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha de creación del perfil

    def __str__(self):
        return self.usuario.username

class Deporte(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)  # Descripción del deporte
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro

    def __str__(self):
        return self.nombre

class Partido(models.Model):
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    equipo1 = models.CharField(max_length=100)
    equipo2 = models.CharField(max_length=100)
    fecha_partido = models.DateTimeField()
    ubicacion = models.CharField(max_length=255, blank=True, null=True)  # Ubicación del partido
    estado = models.CharField(max_length=50, choices=[
        ('programado', 'Programado'),
        ('en_curso', 'En Curso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ], default='programado')  # Estado del partido

    def __str__(self):
        return f"{self.equipo1} vs {self.equipo2} el {self.fecha_partido}"

class Prediccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    ganador_predicho = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la predicción
    puntos_otorgados = models.IntegerField(default=0)  # Puntos otorgados si la predicción es correcta

    def __str__(self):
        return f"{self.usuario.username} predice que {self.ganador_predicho} ganará el partido {self.partido}"


class Notificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    leido = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(blank=True, null=True, upload_to='fotos_perfil')
    biografia = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    puntos = models.IntegerField(default=0)  # Campo para almacenar los puntos

    def __str__(self):
        return self.usuario.username



# class Notificacion(models.Model):
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     mensaje = models.TextField()
#     leido = models.BooleanField(default=False)
#     fecha_creacion = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Notificación para {self.usuario.username}'

