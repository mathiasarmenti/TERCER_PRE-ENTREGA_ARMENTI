from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, VentaForm
from .models import Cliente, Producto, Venta

def inicio(request):
    return render(request, 'base.html')

def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes.html', {'form': form})

def productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'productos.html', {'form': form})

def busqueda(request):
    if 'q' in request.GET:
        query = request.GET['q']
        clientes = Cliente.objects.filter(nombre__icontains=query)
        productos = Producto.objects.filter(nombre__icontains=query)
        return render(request, 'busqueda.html', {'clientes': clientes, 'productos': productos})
    return render(request, 'busqueda.html')
