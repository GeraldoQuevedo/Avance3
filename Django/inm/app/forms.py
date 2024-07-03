# app/forms.py

from django import forms
from .models import Periodista

class PeriodistaForm(forms.ModelForm):
    class Meta:
        model = Periodista
        fields = ['rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'email']
