from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Producto, Categoria, Etiqueta
from .forms import ProductoForm, CategoriaForm, EtiquetaForm


def index(request):
    return render(request, 'index.html')


# Productos

class ProductoListView(ListView):
    model = Producto
    template_name = "productos/lista.html"
    context_object_name = "productos"


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/crear.html"
    success_url = reverse_lazy('lista_productos')


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/detalle.html"
    context_object_name = "producto"


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/editar.html"
    success_url = reverse_lazy('lista_productos')


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = "productos/eliminar.html"
    success_url = reverse_lazy('lista_productos')


# Categorias

class CategoriaListView(ListView):
    model = Categoria
    template_name = "categorias/lista.html"
    context_object_name = "categorias"


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "categorias/formulario.html"
    success_url = reverse_lazy('lista_categorias')


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "categorias/formulario.html"
    success_url = reverse_lazy('lista_categorias')


# class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
#     model = Categoria
#     template_name = "categorias/eliminar.html"
#     success_url = reverse_lazy('lista_categorias')


# Etiquetas

class EtiquetaListView(ListView):
    model = Etiqueta
    template_name = "etiquetas/lista.html"
    context_object_name = "etiquetas"


class EtiquetaCreateView(LoginRequiredMixin, CreateView):
    model = Etiqueta
    form_class = EtiquetaForm
    template_name = "etiquetas/formulario.html"
    success_url = reverse_lazy('lista_etiquetas')


class EtiquetaUpdateView(LoginRequiredMixin, UpdateView):
    model = Etiqueta
    form_class = EtiquetaForm
    template_name = "etiquetas/formulario.html"
    success_url = reverse_lazy('lista_etiquetas')


# class EtiquetaDeleteView(LoginRequiredMixin, DeleteView):
#     model = Etiqueta
#     template_name = "etiquetas/eliminar.html"
#     success_url = reverse_lazy('lista_etiquetas')
