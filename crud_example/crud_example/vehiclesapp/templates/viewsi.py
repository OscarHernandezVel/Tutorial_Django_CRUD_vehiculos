from django.shortcuts import render,HttpResponseRedirect,get_object_or_404

from models import vehiculo
from formis import VehiculoForm

# Create your views here.

def create_view(request):
    context ={}
    form = VehiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/view/")
    
    context['form']= form
    return render(request, "create_view.html", context)

def list_view(request):
    context ={}
    context["dataset"] = vehiculo.objects.all()
         
    return render(request, "list_view.html", context)
def update_view(request, id):
    context ={}

    obj = get_object_or_404(vehiculo, id=id)

    form = VehiculoForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/view/")
    
    context["form"] = form
    return render(request, "update_view.html", context)

def delete_view(request, id):
    context ={}
    
    obj = get_object_or_404(vehiculo, id=id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/view/")
    
    return render(request, "delete_view.html", context)