# predictions/forms.py
from django import forms
from django.utils import timezone
from .models import Prediccion, Partido

from django import forms
from django.utils import timezone
from .models import Prediccion

class PrediccionForm(forms.ModelForm):
    class Meta:
        model = Prediccion
        fields = ['ganador_predicho']
        widgets = {
            'ganador_predicho': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ResultadoPartidoForm(forms.Form):
    resultado = forms.ChoiceField(choices=[('equipo1', 'Equipo 1'), ('equipo2', 'Equipo 2')], label='Resultado')


class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['deporte', 'equipo1', 'equipo2', 'fecha_partido', 'ubicacion', 'estado']
        widgets = {
            'deporte': forms.Select(attrs={'class': 'form-control'}),
            'equipo1': forms.TextInput(attrs={'class': 'form-control'}),
            'equipo2': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_partido': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

