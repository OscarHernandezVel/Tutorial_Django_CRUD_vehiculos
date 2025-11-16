from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import vehiculo
from django import forms


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = vehiculo
        fields = ['placa', 'marca', 'color', 'modelo']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: ABC123'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Toyota'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 2023'}),
        }


def home(request):
    """Vista de inicio"""
    return render(request, 'hello_world.html')


def list_view(request):
    """Lista todos los vehículos"""
    vehiculos = vehiculo.objects.all()
    return render(request, 'list_viewi.html', {'vehiculos': vehiculos})


def create_view(request):
    """Crea un nuevo vehículo"""
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo creado exitosamente.')
            return redirect('list')
    else:
        form = VehiculoForm()
    
    return render(request, 'vehiculo_form.html', {'form': form})


def update_view(request, id):
    """Actualiza un vehículo existente"""
    vehicle = get_object_or_404(vehiculo, id=id)
    
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo actualizado exitosamente.')
            return redirect('list')
    else:
        form = VehiculoForm(instance=vehicle)
    
    return render(request, 'vehiculo_form.html', {'form': form})


def delete_view(request, id):
    """Elimina un vehículo"""
    vehicle = get_object_or_404(vehiculo, id=id)
    
    if request.method == 'POST':
        vehicle.delete()
        messages.success(request, 'Vehículo eliminado exitosamente.')
        return redirect('list')
    
    return render(request, 'vehiculo_confirm_delete.html', {'vehiculo': vehicle})
