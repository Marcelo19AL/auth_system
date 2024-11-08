from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Partido, Prediccion, Notificacion, PerfilUsuario
from .forms import PrediccionForm, ResultadoPartidoForm,PartidoForm
from django.utils import timezone
from django.contrib import messages

@login_required
def lista_partidos(request):
    # Filtra partidos programados a partir de hoy
    hoy = timezone.now().date()
    partidos = Partido.objects.filter(fecha_partido__date__gte=hoy, estado='programado')
    return render(request, 'predictions/lista_partidos.html', {'partidos': partidos})

@login_required
def hacer_prediccion(request, partido_id):
    partido = get_object_or_404(Partido, id=partido_id)

    # Verificar que el partido está programado y no ha pasado
    if partido.fecha_partido < timezone.now() or partido.estado != 'programado':
        return redirect('lista_partidos')  # Redirigir si el partido no es válido

    if request.method == 'POST':
        form = PrediccionForm(request.POST)
        if form.is_valid():
            prediccion = form.save(commit=False)
            prediccion.partido = partido  # Asignar el partido directamente
            prediccion.usuario = request.user
            prediccion.fecha_creacion = timezone.now()
            prediccion.save()
            return redirect('lista_predicciones')
    else:
        form = PrediccionForm()

    return render(request, 'predictions/hacer_prediccion.html', {'form': form, 'partido': partido})


@login_required
def lista_predicciones(request):
    predicciones = Prediccion.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'predictions/lista_predicciones.html', {'predicciones': predicciones})

@login_required
def lista_notificaciones(request):
    notificaciones = Notificacion.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'predictions/lista_notificaciones.html', {'notificaciones': notificaciones})

@login_required
def lista_predicciones(request):
    # Obtiene las predicciones del usuario actual
    predicciones = Prediccion.objects.filter(usuario=request.user)
    return render(request, 'predictions/lista_predicciones.html', {'predicciones': predicciones})


@login_required
def actualizar_resultado(request, partido_id):
    partido = get_object_or_404(Partido, id=partido_id)

    if request.method == 'POST':
        form = ResultadoPartidoForm(request.POST)
        if form.is_valid():
            resultado = form.cleaned_data['resultado']
            partido.ganador = resultado  # Suponiendo que se añade un campo "ganador" en el modelo Partido
            partido.estado = 'completado'
            partido.save()

            # Verificar predicciones correctas y actualizar puntos
            predicciones_correctas = Prediccion.objects.filter(partido=partido, ganador_predicho=resultado)

            for prediccion in predicciones_correctas:
                perfil = get_object_or_404(PerfilUsuario, usuario=prediccion.usuario)
                perfil.puntos += 10  # Asignar 10 puntos por predicción correcta
                perfil.save()

            return redirect('mis_partidos')  # Redirige a la lista de partidos

    else:
        form = ResultadoPartidoForm()

    return render(request, 'predictions/actualizar_resultado.html', {'form': form, 'partido': partido})


@login_required
def agregar_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_partidos')  # Redirigir a la lista de partidos
    else:
        form = PartidoForm()
    
    return render(request, 'predictions/agregar_partido.html', {'form': form})
