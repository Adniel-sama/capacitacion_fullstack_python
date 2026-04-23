from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tarea/crear/', views.crear, name='crear'),
    path('tarea/editar/<str:nombre>/', views.editar, name='editar'),
    path('tarea/detalle/<str:nombre>/', views.detalle, name='detalle'),
    path('tarea/borrar/<str:nombre>/', views.borrar, name='borrar'),
    #path('tarea/todas/', views.todas, name='todas'),
]

