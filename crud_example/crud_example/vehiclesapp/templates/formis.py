# forms.py

from django import forms
from models import vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = vehiculo
        fields = ["placa", "marca", "color", "modelo"]
        labels = {
            "placa": "Placa del Vehículo",
            "marca": "Marca del Vehículo",
            "color": "Color del Vehículo",
            "modelo": "Modelo del Vehículo",
        }
        widgets = {
            "placa": forms.TextInput(attrs={"class": "form-control"}),
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "color": forms.Select(attrs={"class": "form-control"}),
            "modelo": forms.NumberInput(attrs={"class": "form-control"}),
        }
