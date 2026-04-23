from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('productos/', ProductoListView.as_view(), name='lista_productos'),
    path('productos/crear/', ProductoCreateView.as_view(), name='crear_producto'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='detalle_producto'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='eliminar_producto'),

    path('categorias/', CategoriaListView.as_view(), name='lista_categorias'),
    path('categorias/crear/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='editar_categoria'),
    #path('categorias/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='eliminar_categoria'),

    path('etiquetas/', EtiquetaListView.as_view(), name='lista_etiquetas'),
    path('etiquetas/crear/', EtiquetaCreateView.as_view(), name='crear_etiqueta'),
    path('etiquetas/<int:pk>/editar/', EtiquetaUpdateView.as_view(), name='editar_etiqueta'),
    #path('etiquetas/<int:pk>/eliminar/', EtiquetaDeleteView.as_view(), name='eliminar_etiqueta'),
]
